from flask_frozen import Freezer
from assignments.assign09.assign09_flask import app

# 빌드 설정 추가
app.config["FREEZER_DESTINATION_IGNORE_DOTTED"] = True
# 쿼리 스트링을 사용하는 경우 파일명 생성을 돕는 설정
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
