from flask_frozen import Freezer
from assignments.assign09.assign09_flask import app

# 1. 확장자 미매칭 경고 해결 및 폴더 구조화 설정
app.config["FREEZER_DESTINATION_IGNORE_DOTTED"] = True
# 2. (선택) 로컬에서 HTML 파일을 직접 열 때 경로가 깨지지 않게 함
app.config["FREEZER_RELATIVE_URLS"] = True

freezer = Freezer(app)


@freezer.register_generator
def search():
    keywords = ["python", "django", "javascript"]
    for keyword in keywords:
        yield {"keyword": keyword}


if __name__ == "__main__":
    # URL 생성을 강제로 쿼리스트링 형태로 매칭시키기 위한 설정
    # 만약 위 generator가 작동하지 않는다면 아래처럼 직접 URL을 지정할 수도 있습니다.

    print("🚀 정적 빌드 시작...")
    freezer.freeze()
