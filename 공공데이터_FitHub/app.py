from flask import Flask, request, redirect, url_for, render_template, flash, jsonify, session
import pandas as pd
from datetime import datetime
import os
import re

app = Flask(__name__)
app.secret_key = "secret_key_for_flash"

FILE_PATH = r"C:\Users\seong\OneDrive\바탕 화면\공공데이터_웹_중간중간중간\user_data.csv"

def load_users():
    if os.path.exists(FILE_PATH):
        return pd.read_csv(FILE_PATH)
    else:
        return pd.DataFrame(columns=["username", "password", "name", "gender", "birthdate", "basic_living", "disability", "veteran", "minor_children", "max_discount"])

# 사용자 정보 저장 (CSV 파일에 저장)
def save_users(df):
    df.to_csv(FILE_PATH, index=False)

# 사용자 정보 DataFrame
users = load_users()

# 로그인한 사용자 정보 저장 (임시)
current_user = None

# 예약된 강좌 저장
reservations = {}

# 할인율 계산 함수
def calculate_discount(row):
    discounts = []

    # 장애인 여부 (50%)
    if row['disability']:
        discounts.append(50)  # 장애 여부가 True이면 50% 할인
    
    # 성별 (만 12~55, 여성 10%)
    birthdate = pd.to_datetime(row['birthdate'])
    age = (pd.Timestamp.now() - birthdate).days // 365  # 나이 계산 (연도 단위)
    if row['gender'] == 1 and 12 <= age <= 55:  # 여성이고, 나이가 12~55 사이이면
        discounts.append(10)  # 여성에게 10% 할인
    
    # 기초수급자 여부 (50%)
    if row['basic_living']:
        discounts.append(50)  # 기초수급자 여부가 True이면 50% 할인
    
    # 국가보훈자 여부 (50%)
    if row['veteran']:
        discounts.append(50)  # 국가보훈자 여부가 True이면 50% 할인
    
    # 자녀 유무 및 명수 (30%)
    if row['minor_children'] != '0':
        discounts.append(30)  # 자녀가 있으면 30% 할인
    
    # 가장 큰 할인율 계산
    max_discount = max(discounts) if discounts else 0
    return max_discount

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
    global current_user  # 전역 변수 사용 (현재 로그인한 사용자)
    if request.method == 'POST':
        username = request.form.get('username')  # 입력된 사용자 아이디
        password = request.form.get('password')  # 입력된 비밀번호

        # 1. 아이디가 'user_data.csv'에 존재하는지 확인
        if username in users['username'].values:
            # 2. 아이디가 존재하면 비밀번호 확인
            user_row = users[users['username'] == username].iloc[0]
            if user_row['password'] == password:
                current_user = username  # 로그인한 사용자 저장
                session['current_user'] = username  # 세션에 저장하여 로그인 상태 유지
                return redirect(url_for('home'))  # 홈 화면으로 리다이렉트
            else:
                flash("비밀번호가 틀렸습니다.")  # 비밀번호가 틀린 경우
                return redirect(url_for('login'))  # 로그인 페이지로 리다이렉트
        else:
            flash("아이디가 존재하지 않습니다.")  # 아이디가 없는 경우
            return redirect(url_for('login'))  # 로그인 페이지로 리다이렉트
    return render_template('login.html')  # GET 요청 시 로그인 페이지 렌더링

@app.route('/logout')
def logout():
    session.pop("current_user", None)  # 세션에서 사용자 정보 제거
    flash("로그아웃되었습니다.")
    return redirect(url_for('login'))

@app.route('/join', methods=['GET', 'POST'])
def join():
    global users  # users를 전역 변수로 사용
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        name = request.form.get('name')  # 회원가입 시 이름 추가
        gender = 0 if request.form.get('gender') == '남' else 1
        birthdate = request.form.get('birthdate')
        
        # 할인 혜택 정보 받아오기
        basic_living = request.form.get('basic_living') == 'on'  # 기초생활 수급자 여부
        disability = request.form.get('disability') == 'on'  # 장애 여부
        veteran = request.form.get('veteran') == 'on'  # 국가유공자 여부
        minor_children = request.form.get('minor_children')  # 미성년 자녀 수

        # 비밀번호 조건 체크: 최소 8자 이상, 영문자 + 숫자 포함
        if not re.search(r'[a-zA-Z]', password):  # 영문자가 포함되지 않으면
            flash("비밀번호는 최소한 하나의 영문자를 포함해야 합니다.")
            return redirect(url_for('join'))
        if not re.search(r'[0-9]', password):  # 숫자가 포함되지 않으면
            flash("비밀번호는 최소한 하나의 숫자를 포함해야 합니다.")
            return redirect(url_for('join'))
        if len(password) < 8:  # 비밀번호가 8자 미만이면
            flash("비밀번호는 최소 8자 이상이어야 합니다.")
            return redirect(url_for('join'))

        # 아이디 중복 확인
        if username in users['username'].values:
            flash("이미 존재하는 아이디입니다.")
            return redirect(url_for('join'))
        else:
            # 사용자 정보를 DataFrame에 추가
            new_user = pd.DataFrame([[username, password, name, gender, birthdate, basic_living, disability, veteran, minor_children]],
                                    columns=["username", "password", "name", "gender", "birthdate", "basic_living", "disability", "veteran", "minor_children"])

            # 할인율 계산
            new_user["max_discount"] = new_user.apply(calculate_discount, axis=1)

            # 기존 사용자 데이터와 결합하여 업데이트
            users = pd.concat([users, new_user], ignore_index=True)  # DataFrame에 새 사용자 추가
            
            # 업데이트된 DataFrame을 CSV 파일에 저장
            save_users(users)
            
            flash("회원가입이 완료되었습니다. 로그인하세요.")
            return redirect(url_for('login'))
    
    return render_template('join.html')


@app.route('/mypage')
def mypage():
    if current_user:
        user_info = users[users["username"] == current_user].iloc[0]
        
        # 회원가입 시 제공된 정보와 할인율을 MyPage에 출력
        name = user_info["name"]
        username = current_user
        gender = "남" if user_info["gender"] == 0 else "여"
        birthdate = user_info["birthdate"]
        basic_living = "기초수급자" if user_info["basic_living"] else "아님"
        disability = "장애인" if user_info["disability"] else "아님"
        veteran = "국가유공자" if user_info["veteran"] else "아님"
        minor_children = user_info["minor_children"] if user_info["minor_children"] else "없음"
        max_discount = user_info["max_discount"]

        return render_template('mypage.html', name=name, username=username, gender=gender, birthdate=birthdate,
                               basic_living=basic_living, disability=disability, veteran=veteran,
                               minor_children=minor_children, max_discount=max_discount)
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
