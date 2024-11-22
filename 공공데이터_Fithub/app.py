from flask import Flask, request, redirect, url_for, render_template, flash, jsonify
import pandas as pd
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret_key_for_flash"

# 사용자 데이터 저장
users = {"test": {"password": "1234", "name": "홍길동"}}  # 예시: {"아이디": {"password": "비밀번호", "name": "이름"}}

# 로그인한 사용자 정보 저장 (임시)
current_user = None

# 예약된 강좌 저장
reservations = {}

# 데이터 불러오기 및 전처리
data = pd.read_csv("C:/Users/seong/OneDrive/바탕 화면/올림픽수영장 강좌정보.csv", encoding='cp949')
data['수강료'] = data['수강료'].fillna(0).astype(int)
data['정원'] = data['정원'].fillna(0).astype(int)

time_split = data['시작시간'].str.split('-', n=1, expand=True)
data['시작시간'] = time_split[0]
data['끝나는시간'] = time_split[1]
data['시작시간'] = pd.to_datetime(data['시작시간'], format='%H:%M').dt.time
data['끝나는시간'] = pd.to_datetime(data['끝나는시간'], format='%H:%M').dt.time

cols = list(data.columns)
cols.insert(7, cols.pop(13))
data = data[cols]

data['기간종료일'] = data['기간종료일'].replace('9999-12-31', '2099-12-31')
data['기간시작일'] = pd.to_datetime(data['기간시작일'], errors='coerce')
data['기간종료일'] = pd.to_datetime(data['기간종료일'], errors='coerce')

current_date = pd.Timestamp(datetime.now().date())
ongoing_courses = data[(data['기간시작일'] <= current_date) & (data['기간종료일'] >= current_date)]
ongoing_courses = ongoing_courses.reset_index(drop=True)

@app.route('/home')
def home():
    global reservations, current_user
    user_reservations = reservations.get(current_user, [])
    
    # 시간표 생성: 6:00부터 24:00까지, 월~일
    timetable = {f"{hour:02d}": {day: '' for day in ['월', '화', '수', '목', '금', '토', '일']}
                 for hour in range(6, 25)}

    # 예약된 강좌 시간표에 반영
    for course in user_reservations:
        days = course['수강요일'].split(',')  # 강좌 요일을 리스트로 분리
        start_hour = int(course['시작시간'].split(':')[0])  # 시작 시간의 시
        for day in days:
            if day in timetable[f"{start_hour:02d}"]:
                timetable[f"{start_hour:02d}"][day] = course['종목']  # 종목명만 추가

    return render_template('home.html', reservations=user_reservations, timetable=timetable)

def create_timetable(reservations):
    """
    예약 데이터를 기반으로 시간표 데이터를 생성합니다.
    시간: 9시~18시, 요일: 월~일
    """
    # 기본 시간표 구조 생성
    timetable = {hour: {day: None for day in ['월', '화', '수', '목', '금', '토', '일']} for hour in range(9, 19)}

    for course in reservations:
        # 강좌의 수강 요일과 시간 파싱
        days = course['수강요일'].split(',')  # 예: "월,수,금"
        start_time = pd.to_datetime(course['시작시간'], format='%H:%M').hour
        end_time = pd.to_datetime(course['끝나는시간'], format='%H:%M').hour

        # 해당 요일과 시간에 강좌를 추가
        for day in days:
            for hour in range(start_time, end_time):
                timetable[hour][day] = course['강좌명']

    return timetable

@app.route('/reservation')
def reservation():
    global ongoing_courses

    # '시작시간'과 '끝나는시간'이 문자열인지 확인하고 변환
    if not isinstance(ongoing_courses['시작시간'].iloc[0], str):
        ongoing_courses['시작시간'] = ongoing_courses['시작시간'].apply(lambda x: x.strftime('%H:%M') if pd.notnull(x) else None)
        ongoing_courses['끝나는시간'] = ongoing_courses['끝나는시간'].apply(lambda x: x.strftime('%H:%M') if pd.notnull(x) else None)


    # JSON 형식으로 데이터를 템플릿으로 전달
    return render_template('reservation.html', courses=ongoing_courses.to_dict(orient='records'))

@app.route('/', methods=['GET', 'POST'])
def login():
    global current_user
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # 로그인 검증
        if username in users and users[username]["password"] == password:
            current_user = username  # 현재 로그인한 사용자 저장
            return redirect(url_for('home'))
        else:
            flash("아이디 또는 비밀번호가 잘못되었습니다.")
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        name = request.form.get('name')  # 회원가입 시 이름 추가

        if username in users:
            flash("이미 존재하는 아이디입니다.")
            return redirect(url_for('join'))
        else:
            # 사용자 정보 저장
            users[username] = {"password": password, "name": name}
            flash("회원가입이 완료되었습니다. 로그인하세요.")
            return redirect(url_for('login'))
    return render_template('join.html')


@app.route('/mypage')
def mypage():
    if current_user:
        user_info = users[current_user]
        return render_template('mypage.html', name=user_info["name"], username=current_user)
    else:
        flash("로그인이 필요합니다.")
        return redirect(url_for('login'))

@app.route('/filter_courses', methods=['POST'])
def filter_courses():
    global ongoing_courses

    category = request.json.get('category', '')
    selected_days = request.json.get('selected_days', [])
    start_time = request.json.get('start_time', None)

    filtered_courses = ongoing_courses.copy()

    # 필터링: 종목
    if category:
        filtered_courses = filtered_courses[filtered_courses['종목'] == category]

    # 필터링: 수강요일
    if selected_days:
        filtered_courses = filtered_courses[
            filtered_courses['수강요일'].apply(lambda x: all(day in x for day in selected_days))
        ]

    # 필터링: 시작 시간
    if start_time:
        # 문자열로 저장된 시간과 비교
        filtered_courses = filtered_courses[
            filtered_courses['시작시간'].apply(lambda x: pd.to_datetime(x, format='%H:%M').time()) >= pd.to_datetime(start_time, format='%H:%M').time()
        ]

    filtered_courses = filtered_courses.to_dict(orient='records')
    return jsonify(filtered_courses)

@app.route('/reserve', methods=['POST'])
def reserve():
    global reservations, current_user

    # 현재 사용자가 로그인 상태인지 확인
    if not current_user:
        return jsonify({"success": False, "message": "로그인이 필요합니다."}), 403

    course = request.json.get('course')
    if not course:
        return jsonify({"success": False, "message": "강좌 정보가 누락되었습니다."}), 400

    # 사용자별 예약 목록 가져오기
    user_reservations = reservations.get(current_user, [])

    # 시간 충돌 체크 함수
    def is_time_conflict(existing_course, new_course):
        existing_start = pd.to_datetime(existing_course['시작시간'], format='%H:%M').time()
        existing_end = pd.to_datetime(existing_course['끝나는시간'], format='%H:%M').time()
        new_start = pd.to_datetime(new_course['시작시간'], format='%H:%M').time()
        new_end = pd.to_datetime(new_course['끝나는시간'], format='%H:%M').time()
        return not (new_end <= existing_start or new_start >= existing_end)

    # 예약된 강좌와 시간 충돌 확인
    for reserved_course in user_reservations:
        if is_time_conflict(reserved_course, course):
            return jsonify({"success": False, "message": "이미 예약한 강좌와 시간이 겹칩니다."})

    # 시간 충돌이 없으면 예약 추가
    if current_user not in reservations:
        reservations[current_user] = []
    reservations[current_user].append(course)

    return jsonify({"success": True, "message": "예약되었습니다."})

if __name__ == '__main__':
    app.run(debug=True)
