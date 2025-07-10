import streamlit as st

# 질환군별 사이토카인 정상범위 및 환자범위 설정
def get_disease_ranges(disease):
    # 류마티스 관절염 (RA) 범위
    if disease == "RA":
        return {
            "TNF-α": {"normal": (0, 15), "patient": (30, 100)},
            "IL-6": {"normal": (0, 5), "patient": (10, 200)},
            "IL-1β": {"normal": (0, 3), "patient": (5, 50)}
        }

    # 전신 홍반 루푸스 (SLE) 범위
    elif disease == "SLE":
        return {
            "IL-6": {"normal": (0, 5), "patient": (10, 50)},
            "IL-10": {"normal": (0, 10), "patient": (15, 100)},
            "TNF-α": {"normal": (0, 15), "patient": (20, 60)}
        }

    # 크론병 (Crohn's Disease) 범위
    elif disease == "Crohn's":
        return {
            "TNF-α": {"normal": (0, 15), "patient": (30, 100)},
            "IL-12": {"normal": (0, 5), "patient": (20, 100)},
            "IL-6": {"normal": (0, 5), "patient": (20, 200)}
        }

# 예측 시스템 기능
def predict(disease, cytokine_values):
    ranges = get_disease_ranges(disease)
    
    result = {}
    for cytokine, value in cytokine_values.items():
        normal_range = ranges[cytokine]["normal"]
        patient_range = ranges[cytokine]["patient"]
        
        # 정상범위와 환자범위 비교
        if normal_range[0] <= value <= normal_range[1]:
            result[cytokine] = "Normal"
        elif patient_range[0] <= value <= patient_range[1]:
            result[cytokine] = "Patient Range"
        else:
            result[cytokine] = "Out of Range"

    return result

# Streamlit 앱 코드
def app():
    st.title("자가면역 질환 사이토카인 예측 시스템")
    disease = st.selectbox("질환을 선택하세요", ["RA", "SLE", "Crohn's"])
    
    # 각 질환에 맞는 입력 필드 생성
    if disease == "RA":
        cytokines = ["TNF-α", "IL-6", "IL-1β"]
    elif disease == "SLE":
        cytokines = ["IL-6", "IL-10", "TNF-α"]
    else:
        cytokines = ["TNF-α", "IL-12", "IL-6"]

    cytokine_values = {}
    
    for cytokine in cytokines:
        value = st.number_input(f"{cytokine} 값을 입력하세요 (pg/mL)", min_value=0.0, step=0.1)
        cytokine_values[cytokine] = value

    # 예측 버튼
    if st.button("예측하기"):
        result = predict(disease, cytokine_values)
        st.write("예측 결과:")
        for cytokine, status in result.items():
            st.write(f"{cytokine}: {status}")

if __name__ == "__main__":
    app()