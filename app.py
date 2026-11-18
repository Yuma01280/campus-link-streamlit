import streamlit as st

# ==========================================
# 1. 페이지 기본 설정
# ==========================================

st.set_page_config(
    page_title="Campus Link",
    page_icon="🎓",
    layout="wide"
)

# ==========================================
# 2. Campus Link 디자인 CSS
# ==========================================

st.html(
    """
    <style>

        /* 전체 페이지 */
        .stApp {
            background-color: #F7F9FD;
            color: #1E293B;
        }

        .block-container {
            max-width: 1150px;
            padding-top: 3rem;
            padding-bottom: 4rem;
        }

        /* 기본 제목 */
        h1, h2, h3 {
            color: #172554 !important;
        }

        /* 메인 소개 영역 */
        .cl-hero {
            background: linear-gradient(
                135deg,
                #EAF2FF 0%,
                #FFFFFF 100%
            );

            border: 1px solid #D9E6FF;
            border-radius: 22px;

            padding: 48px 45px;
            margin-bottom: 45px;

            box-shadow: 0 8px 28px rgba(
                37, 99, 235, 0.06
            );
        }

        /* 상단 작은 라벨 */
        .cl-eyebrow {
            color: #2563EB;

            font-size: 0.78rem;
            font-weight: 800;

            letter-spacing: 2px;
            margin-bottom: 18px;
        }

        /* 메인 제목 */
        .cl-hero h1 {
            font-size: 2.5rem;
            font-weight: 850;

            line-height: 1.4;
            letter-spacing: -1.5px;

            color: #172554 !important;

            margin-bottom: 22px;
        }

        .cl-hero h1 span {
            color: #2563EB;
        }

        /* 소개 설명 */
        .cl-hero p {
            color: #475569;

            font-size: 1.02rem;
            line-height: 1.9;

            margin: 0;
        }

        /* 섹션 설명 */
        .cl-section-intro {
            color: #64748B;

            font-size: 0.96rem;
            line-height: 1.8;

            margin-top: -5px;
            margin-bottom: 25px;
        }

        /* 기능 소개 카드 */
        .cl-card {
            background: #FFFFFF;

            border: 1px solid #DFE7F3;
            border-radius: 16px;

            padding: 26px 23px;
            margin-bottom: 15px;

            min-height: 205px;

            box-shadow: 0 4px 14px rgba(
                15, 23, 42, 0.035
            );

            transition: all 0.2s ease;
        }

        /* 카드 마우스 효과 */
        .cl-card:hover {
            border-color: #93B4FF;

            transform: translateY(-3px);

            box-shadow: 0 9px 24px rgba(
                37, 99, 235, 0.1
            );
        }

        /* 카드 아이콘 */
        .cl-icon {
            font-size: 1.85rem;
            margin-bottom: 14px;
        }

        /* 카드 제목 */
        .cl-card-title {
            font-size: 1.05rem;
            font-weight: 750;

            color: #1E3A8A;

            margin-bottom: 10px;
        }

        /* 카드 설명 */
        .cl-card-desc {
            font-size: 0.9rem;

            color: #64748B;
            line-height: 1.75;
        }

        /* 사용자별 서비스 박스 */
        .cl-role {
            background: #EAF2FF;

            border: 1px solid #CFE0FF;
            border-left: 5px solid #2563EB;

            border-radius: 13px;

            padding: 24px 27px;
            margin-top: 13px;
        }

        .cl-role strong {
            color: #1D4ED8;
            font-size: 1.05rem;
        }

        .cl-role p {
            color: #355072;

            margin: 8px 0 0;
            line-height: 1.7;
        }

        /* 하단 안내 */
        .cl-footer {
            border-top: 1px solid #DAE3F0;

            padding-top: 18px;
            margin-top: 34px;

            font-size: 0.86rem;
            color: #7B8CA5;

            text-align: center;
            line-height: 1.9;
        }

        /* 모바일 반응형 */
        @media (max-width: 768px) {

            .block-container {
                padding: 1.5rem 1rem;
            }

            .cl-hero {
                padding: 30px 23px;
                border-radius: 17px;
            }

            .cl-hero h1 {
                font-size: 1.85rem;
            }

            .cl-hero p {
                font-size: 0.94rem;
            }

            .cl-card {
                min-height: 0;
                padding: 20px;
            }

            .cl-role {
                padding: 20px;
            }
        }

    </style>
    """,
)


# ==========================================
# 3. Campus Link 메인 소개
# ==========================================

st.html(
    """
    <div class="cl-hero">

        <div class="cl-eyebrow">
            CAMPUS LINK · ACADEMIC COMMUNITY
        </div>

        <h1>
            학교에서 시작되는 질문,<br>
            <span>사람과 기회로 이어지다.</span>
        </h1>

        <p>
            Campus Link는
            <b>재학생·교수·졸업생</b>을 연결하는
            학교 기반 학술 커뮤니티입니다.
            <br><br>

            궁금한 내용을 질문하고,
            수업 경험을 나누고,
            프로젝트와 스터디의 동료를 찾으며
            <br>

            대학 안에서 지식과 경험이
            이어지는 공간을 지향합니다.
        </p>

    </div>
    """,
)


# ==========================================
# 4. 주요 기능 소개
# ==========================================

st.header("📌 주요 기능")

st.markdown(
    """
    <p class="cl-section-intro">
        학교생활에 필요한 정보와 학술 활동을
        한곳에서 연결합니다.
    </p>
    """,
    unsafe_allow_html=True,
)

features = [
    (
        "🎓",
        "학교 기반 회원가입·로그인",
        "소속 학교를 바탕으로 구성원이 "
        "학술 커뮤니티에 참여합니다.",
    ),
    (
        "💬",
        "학술 질문과 답변",
        "학생이 질문을 올리고 교수와 구성원이 "
        "지식과 경험을 공유합니다.",
    ),
    (
        "📚",
        "수업 후기",
        "수업에서 얻은 경험을 기록하고 "
        "같은 학교 구성원과 나눕니다.",
    ),
    (
        "🤝",
        "학술 활동 모집",
        "프로젝트·공모전·스터디 모집글을 "
        "작성하고 지원·참여합니다.",
    ),
    (
        "👤",
        "마이페이지",
        "작성한 글과 모집 지원·참여 현황 등 "
        "자신의 활동을 확인합니다.",
    ),
    (
        "🛡️",
        "신고 및 운영 관리",
        "부적절한 콘텐츠를 신고하고 "
        "관리자가 신고 내용을 검토합니다.",
    ),
]

# 3개씩 2줄 카드 배치
for start in (0, 3):
    cols = st.columns(3, gap="medium")

    for col, (icon, title, desc) in zip(
        cols,
        features[start:start + 3]
    ):
        with col:
            st.html(
                f"""
                <div class="cl-card">
                    <div class="cl-icon">{icon}</div>
                    <div class="cl-card-title">{title}</div>
                    <div class="cl-card-desc">{desc}</div>
                </div>
                """
            )

# ==========================================
# 5. 사용자별 서비스
# ==========================================

st.write("")

st.header("👩‍🎓 사용자별 서비스")

st.markdown(
    """
    <p class="cl-section-intro">
        역할에 따라 Campus Link를 활용하는
        방법을 살펴보세요.
    </p>
    """,
    unsafe_allow_html=True,
)

role = st.selectbox(
    "사용자 유형을 선택하세요.",
    ["재학생", "교수", "졸업생"]
)

role_info = {

    "재학생": (
        "재학생 · 질문에서 참여까지",
        "학술 질문을 등록하고 답변을 확인하며, "
        "수업 후기를 공유하고 "
        "프로젝트·공모전·스터디에 참여할 수 있습니다.",
    ),

    "교수": (
        "교수 · 지식과 경험의 연결",
        "학생들의 학술 질문에 답변하고, "
        "학교 구성원과 학문적 경험을 나누며 "
        "학술 커뮤니티에 참여할 수 있습니다.",
    ),

    "졸업생": (
        "졸업생 · 경험을 후배에게",
        "학교에서 쌓은 경험을 나누고 "
        "학술 질문과 커뮤니티 활동을 통해 "
        "재학생과 연결될 수 있습니다.",
    ),
}

role_title, role_desc = role_info[role]

# 사용자별 서비스 안내 출력
st.html(
    f"""
    <div class="cl-role">
        <strong>{role_title}</strong>
        <p>{role_desc}</p>
    </div>
    """
)


# ==========================================
# 6. 하단 안내
# ==========================================

st.html(
    """
    <div class="cl-footer">

        Campus Link · 소프트웨어융합과 캡스톤 프로젝트

        <br>

        이 페이지는 서비스 소개용이며,
        실제 기능은 Campus Link 웹 서비스에서 제공됩니다.

    </div>
    """,
)