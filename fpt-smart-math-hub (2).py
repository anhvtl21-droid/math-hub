import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="FPT Smart Math Hub",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (FPT Theme)
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        color: #F26F21;
        font-weight: 700;
        text-align: center;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #2B3990;
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #F26F21;
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">📐 FPT SMART MATH HUB</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Nền tảng Trợ lý Giảng dạy Toán học & Gia sư AI Cá nhân hóa — Trường phổ thông FPT Bắc Giang</div>', unsafe_allow_html=True)

# Tabs navigation
tab_teacher, tab_student = st.tabs(["👨‍🏫 Dành cho Giáo viên (Teacher Dashboard)", "🎓 Dành cho Học sinh (Student Workspace)"])

with tab_teacher:
    st.header("👨‍🏫 Bảng Điều Khiển Giảng Dạy & Biên Soạn")
    
    sub_tab1, sub_tab2 = st.tabs(["📝 1. Sinh Đề Thi Theo Ma Trận Tùy Chỉnh", "📊 2. Chẩn Đoán Lỗ Hổng Kiến Thức (Upload Excel/CSV)"])
    
    # ---------------- TAB 1: SINH ĐỀ THI ----------------
    with sub_tab1:
        col_input, col_matrix = st.columns([1, 1])
        
        with col_input:
            st.subheader("📌 Thông tin chung bài thi")
            khoi = st.selectbox("Chọn Khối lớp", ["Toán 10", "Toán 11", "Toán 12"], index=0)
            chu_de = st.text_input("Chủ đề / Bài học", "Đồ thị hàm số bậc hai")
            so_cau = st.number_input("Tổng số câu hỏi trắc nghiệm", min_value=5, max_value=50, value=10, step=5)
            hinh_thuc = st.radio("Hình thức đáp án", ["Trắc nghiệm 4 lựa chọn (A, B, C, D)", "Trắc nghiệm Đúng/Sai", "Tự luận"])

        with col_matrix:
            st.subheader("🎯 Tùy chỉnh Ma trận Tỷ lệ Mức độ Năng lực (%)")
            pct_nb = st.slider("% Nhận biết", 0, 100, 40, step=5)
            pct_th = st.slider("% Thông hiểu", 0, 100, 30, step=5)
            pct_vd = st.slider("% Vận dụng", 0, 100, 20, step=5)
            pct_vdc = st.slider("% Vận dụng cao", 0, 100, 10, step=5)
            
            tong_pct = pct_nb + pct_th + pct_vd + pct_vdc
            
            if tong_pct == 100:
                st.success(f"✅ Tổng tỷ lệ ma trận: **{tong_pct}%** (Hợp lệ)")
            else:
                st.error(f"⚠️ Tổng tỷ lệ hiện tại là **{tong_pct}%**. Vui lòng điều chỉnh sao cho tổng bằng **100%**.")

        st.markdown("---")
        
        # Calculate matrix question count
        n_nb = round(so_cau * pct_nb / 100)
        n_th = round(so_cau * pct_th / 100)
        n_vd = round(so_cau * pct_vd / 100)
        n_vdc = so_cau - (n_nb + n_th + n_vd)

        st.info(f"📊 **Phân bổ câu hỏi thực tế:** Nhận biết: **{n_nb} câu** | Thông hiểu: **{n_th} câu** | Vận dụng: **{n_vd} câu** | Vận dụng cao: **{n_vdc} câu**")

        if st.button("🚀 SINH ĐỀ THI & ĐÁP ÁN MẪU", type="primary", disabled=(tong_pct != 100)):
            st.subheader("📝 Đề thi & Lời giải chi tiết (Xem trước)")
            st.success("Đã sinh bộ đề thành công chuẩn LaTeX kèm Mã dạng bài (Skill ID)!")
            
            st.markdown(f"""
            ### ĐỀ KIỂM TRA MÔN: {chu_de.upper()} — {khoi.upper()}
            *Tổng số câu: {so_cau} câu | Cấu hình: {pct_nb}% NB - {pct_th}% TH - {pct_vd}% VD - {pct_vdc}% VDC*
            
            ---
            **Câu 1 (Nhận biết - Mã: `PARABOL_TUNG_DO_DINH`):** Tọa độ đỉnh $I$ của parabol $(P): y = x^2 - 4x + 3$ là:
            - A. $I(-2; 15)$
            - B. **$I(2; -1)$** *(Đáp án đúng)*
            - C. $I(-2; -1)$
            - D. $I(2; 3)$
            
            *Lời giải:* Hoành độ $x_I = -\\frac{{b}}{{2a}} = 2 \\Rightarrow y_I = 2^2 - 4(2) + 3 = -1$. Đỉnh $I(2; -1)$.
            
            **Câu 2 (Thông hiểu - Mã: `PARABOL_TRUC_DOI_XUNG`):** Phương trình trục đối xứng của parabol $(P): y = -2x^2 + 4x + 1$ là:
            - A. $x = -1$
            - B. **$x = 1$** *(Đáp án đúng)*
            - C. $y = 1$
            - D. $x = 2$
            
            *Lời giải:* Phương trình trục đối xứng là $x = -\\frac{{b}}{{2a}} = -\\frac{{4}}{{2(-2)}} = 1$.
            """)
            
            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                st.download_button("📥 Tải đề thi & đáp án (.DOCX)", data="Sample Word Content", file_name="De_thi_Toan_FPT.docx")
            with col_btn2:
                st.download_button("📥 Tải đề thi PDF (.PDF)", data="Sample PDF Content", file_name="De_thi_Toan_FPT.pdf")

    # ---------------- TAB 2: CHẨN ĐOÁN LỖ HỔNG KIẾN THỨC ----------------
    with sub_tab2:
        st.subheader("🔍 Chẩn Đoán Lỗ Hổng Kiến Thức Bài Kiểm Tra")
        st.write("Tải lên file kết quả bài làm trắc nghiệm của lớp (Excel / CSV) để AI tự động phân tích tỷ lệ học sinh làm sai theo từng dạng bài.")
        
        # Download Template Sample Excel
        sample_df = pd.DataFrame({
            "Mã HS": ["HS01", "HS02", "HS03", "HS04", "HS05", "HS06", "HS07", "HS08", "HS09", "HS10"],
            "Họ và tên": ["Nguyễn Văn A", "Trần Thị B", "Lê Hoàng C", "Phạm Minh D", "Vũ Anh E", "Đỗ Quang F", "Hoàng Thu G", "Bùi Quốc H", "Đặng Ngọc I", "Nông Văn K"],
            "Câu 1 (Tung độ đỉnh)": [1, 0, 1, 0, 0, 1, 0, 1, 0, 0],  # 0 is incorrect
            "Câu 2 (Trục đối xứng)": [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            "Câu 3 (Ứng dụng thực tế)": [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            "Câu 4 (Tham số m - VDC)": [0, 0, 1, 0, 0, 0, 0, 0, 1, 0]
        })
        
        col_down, col_up = st.columns([1, 2])
        with col_down:
            st.info("💡 Chưa có file kết quả?")
            # Allow user to generate dummy template data
            csv_data = sample_df.to_csv(index=False).encode('utf-8-sig')
            st.download_button("📥 Tải File Excel Mẫu Bài Làm (.CSV)", data=csv_data, file_name="Bang_diem_mau_10A1.csv", mime="text/csv")
        
        with col_up:
            uploaded_file = st.file_uploader("📤 Tải lên bảng điểm lớp học (.xlsx hoặc .csv)", type=["xlsx", "csv"])
        
        # If user uploaded a file OR wants to test sample data directly
        df_to_analyze = None
        if uploaded_file is not None:
            try:
                if uploaded_file.name.endswith('.csv'):
                    df_to_analyze = pd.read_csv(uploaded_file)
                else:
                    df_to_analyze = pd.read_excel(uploaded_file)
                st.success(f"✅ Đã tải lên thành công file **{uploaded_file.name}** ({len(df_to_analyze)} học sinh)")
            except Exception as e:
                st.error(f"Lỗi đọc file: {e}")
        else:
            if st.checkbox("🧪 Chạy thử nghiệm với dữ liệu mẫu lớp 10A1 (10 học sinh)"):
                df_to_analyze = sample_df
                st.warning("Đang dùng dữ liệu thử nghiệm mẫu của lớp 10A1.")

        if df_to_analyze is not None:
            st.markdown("---")
            st.subheader("📊 Kết Quả Phân Tích & Chẩn Đoán Lỗ Hổng Kiến Thức")
            
            # Show preview data table
            with st.expander("👀 Xem bảng dữ liệu bài làm chi tiết"):
                st.dataframe(df_to_analyze, use_container_width=True)
            
            # Identify question columns (excluding Student Info)
            question_cols = [col for col in df_to_analyze.columns if col not in ["Mã HS", "Họ và tên", "Lớp", "Tổng điểm"]]
            
            if question_cols:
                total_students = len(df_to_analyze)
                error_rates = {}
                incorrect_counts = {}
                
                for col in question_cols:
                    incorrect_num = (df_to_analyze[col] == 0).sum()
                    incorrect_counts[col] = incorrect_num
                    error_rates[col] = round((incorrect_num / total_students) * 100, 1)
                
                # Convert to DataFrame for visualization
                diag_df = pd.DataFrame({
                    "Dạng bài / Câu hỏi": list(error_rates.keys()),
                    "Số HS làm sai": list(incorrect_counts.values()),
                    "Tỷ lệ hổng kiến thức (%)": list(error_rates.values())
                }).sort_values(by="Tỷ lệ hổng kiến thức (%)", ascending=False)
                
                # Display metrics & Chart
                col_chart, col_summary = st.columns([3, 2])
                
                with col_chart:
                    st.write("**Biểu đồ Tỷ lệ Học sinh Hổng Kiến thức theo Dạng Bài (%)**")
                    st.bar_chart(diag_df.set_index("Dạng bài / Câu hỏi")["Tỷ lệ hổng kiến thức (%)"])
                
                with col_summary:
                    st.write("**🔴 Báo Cáo Chẩn Đoán Sư Phạm (AI Summary)**")
                    
                    # Highlight worst skill
                    top_error = diag_df.iloc[0]
                    st.error(f"⚠️ **Cảnh báo mức 1:** Dạng bài **{top_error['Dạng bài / Câu hỏi']}** có tỷ lệ sai cao nhất: **{top_error['Tỷ lệ hổng kiến thức (%)']}%** ({top_error['Số HS làm sai']}/{total_students} HS).")
                    
                    if len(diag_df) > 1:
                        second_error = diag_df.iloc[1]
                        if second_error['Tỷ lệ hổng kiến thức (%)'] > 30:
                            st.warning(f"⚠️ **Cảnh báo mức 2:** Dạng bài **{second_error['Dạng bài / Câu hỏi']}** có **{second_error['Tỷ lệ hổng kiến thức (%)']}%** HS chưa vững.")
                    
                    st.success("✅ **Đề xuất hành động cho Giáo viên:**")
                    st.write("1. Gửi bài giảng ôn tập lại công thức tính tung độ đỉnh Parabol.")
                    st.write("2. Bấm nút dưới đây để AI tự động giao phiếu 'Vá lỗ hổng' cho các em học sinh làm sai.")
                
                # Action button to create remedial worksheet
                st.markdown("---")
                if st.button("⚡ TỰ ĐỘNG SINH PHIẾU BÀI TẬP 'VÁ LỖ HỔNG' CÁ NHÂN HÓA", type="primary"):
                    st.success(f"🎉 Đã tự động khởi tạo phiếu bài tập bù đắp kiến thức cho dạng bài: **{top_error['Dạng bài / Câu hỏi']}**!")
                    st.markdown("""
                    **Phiếu bài tập luyện tập bổ trợ (Dành cho nhóm HS làm sai):**
                    - *Bài 1:* Cho parabol $(P): y = 2x^2 - 8x + 5$. Tìm tọa độ đỉnh $I$ và tính giá trị $y_I$.
                    - *Bài 2 (Thực tế):* Một vòm cầu hình parabol $y = -0.1x^2 + 4$. Tính độ cao cao nhất ở đỉnh vòm cầu.
                    """)

with tab_student:
    st.header("🎓 Gia sư AI Socratic (Student Workspace)")
    st.write("Dành cho học sinh FPT Bắc Giang ôn luyện và hỏi đáp từng bước.")
    
    st.text_input("💬 Nhập câu hỏi hoặc bài toán em đang gặp vướng mắc:", "Thầy/cô ơi, làm sao để tính tung độ đỉnh parabol khi biết phương trình y = x^2 - 4x + 3 ạ?")
    
    if st.button("💬 Gửi cho Gia sư AI"):
        st.markdown("""
        **🤖 Gia sư AI Socratic:**
        
        Chào em! Để tìm tung độ đỉnh của Parabol $y = x^2 - 4x + 3$, chúng ta không nên học thuộc vẹt mà làm theo 2 bước đơn giản sau:
        
        - **Bước 1:** Em hãy nhớ công thức tính *hoành độ đỉnh* $x_I = -\\frac{b}{2a}$. Với $a = 1, b = -4$, em tính ra $x_I$ bằng bao nhiêu?
        - **Bước 2:** Sau khi có $x_I$, em chỉ cần thế giá trị $x_I$ vừa tìm được vào phương trình ban đầu để tìm $y_I$.
        
        👉 Em hãy thử tính Bước 1 và nhắn lại kết quả cho Gia sư AI nhé!
        """)
