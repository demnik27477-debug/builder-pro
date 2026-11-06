import streamlit as st
from PIL import Image
import pandas as pd

# ---------------------------------------------------------
# 1. Διαμόρφωση Σελίδας & UI Styling
# ---------------------------------------------------------
st.set_page_config(
    page_title="Builder Pro - Commercial Suite",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main-header {
        font-size: 28px;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 5px;
    }
    .sub-header {
        font-size: 15px;
        color: #475569;
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%;
        background-color: #2563EB;
        color: white;
        border-radius: 6px;
        font-weight: bold;
        padding: 10px;
    }
    .cost-card {
        background-color: #F8FAFC;
        border-left: 5px solid #10B981;
        padding: 10px;
        margin-top: 10px;
        border-radius: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. Sidebar (Πλευρικό Μενού)
# ---------------------------------------------------------
st.sidebar.title("🏗️ Builder Pro")
st.sidebar.caption("Super Commercial Edition v3.0")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Επιλέξτε Εργαλείο:",
    [
        "📊 Πίνακας Ελέγχου (Dashboard)",
        "🧱 1. Τοιχοποιία & Υλικά",
        "📐 2. Σκυρόδεμα, Σενάζ & Ανώφλια",
        "🧱 3. Σοβάδες & Επιχρίσματα",
        "🔳 4. Πλακάκια, Δάπεδα & Τσεκολατούρες",
        "🎨 5. Χρώματα & Βαφές",
        "🛡️ 6. Μονώσεις & Στεγάνωση",
        "📄 7. Συγκεντρωτική Αναφορά & Προσφορά"
    ]
)

def add_photo_uploader(label="Φωτογραφία / Σχέδιο Εργασιών"):
    st.markdown("---")
    st.subheader(f"📸 {label}")
    uploaded_file = st.file_uploader(f"Ανεβάστε αρχείο (JPG, PNG)", type=["jpg", "jpeg", "png"], key=label)
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Προεπισκόπηση Σχεδίου / Εργοταξίου", use_container_width=True)
        st.success("✔ Η εικόνα καταχωρήθηκε στη μελέτη!")

# ---------------------------------------------------------
# Dashboard (Πίνακας Ελέγχου)
# ---------------------------------------------------------
if menu == "📊 Πίνακας Ελέγχου (Dashboard)":
    st.markdown('<div class="main-header">🏗️ Builder Pro - Dashboard Έργου & Προϋπολογισμού</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Κεντρικός πίνακας ελέγχου, διαχείρισης και κοστολόγησης εργοταξίου.</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown("### 📋 Βασικές Πληροφορίες Έργου & Εταιρείας")
        c_dash1, c_dash2, c_dash3 = st.columns(3)
        with c_dash1:
            st.text_input("Όνομα Έργου", "Ανακαίνιση Κατοικίας", key="global_project_name")
            st.text_input("Εταιρεία / Εργολάβος", "Τεχνική Κατασκευαστική", key="global_company_name")
        with c_dash2:
            st.text_input("Όνομα Πελάτη", "Ιωάννης Παπαδόπουλος", key="global_client_name")
            st.text_input("ΑΦΜ / Τηλέφωνο Πελάτη", "123456789 - 6900000000", key="global_client_tax")
        with c_dash3:
            st.date_input("Ημερομηνία Έναρξης", key="global_project_date")
            st.number_input("ΦΠΑ Εργασιών / Υλικών (%)", min_value=0, max_value=30, value=24, key="global_vat")

    st.markdown("---")
    st.markdown("### 📊 Κατάσταση Υπολογισμών & Οικονομική Σύνοψη")
    
    total_cost_est = 0.0
    active_calcs = 0

    if "brick_cost" in st.session_state: 
        total_cost_est += st.session_state['brick_cost']
        active_calcs += 1
    if "conc_cost" in st.session_state: 
        total_cost_est += st.session_state['conc_cost']
        active_calcs += 1
    if "plaster_cost" in st.session_state: 
        total_cost_est += st.session_state['plaster_cost']
        active_calcs += 1
    if "tiles_cost" in st.session_state: 
        total_cost_est += st.session_state['tiles_cost']
        active_calcs += 1
    if "paint_cost" in st.session_state: 
        total_cost_est += st.session_state['paint_cost']
        active_calcs += 1
    if "insul_cost" in st.session_state: 
        total_cost_est += st.session_state['insul_cost']
        active_calcs += 1

    vat_rate = st.session_state.get('global_vat', 24) / 100
    total_with_vat = total_cost_est * (1 + vat_rate)

    col_stat1, col_stat2, col_stat3 = st.columns(3)
    col_stat1.metric("Ενότητες σε Ισχύ", f"{active_calcs} / 6")
    col_stat2.metric("Εκτιμώμενο Κόστος (προ ΦΠΑ)", f"{total_cost_est:,.2f} €")
    col_stat3.metric(f"Σύνολο με ΦΠΑ ({st.session_state.get('global_vat', 24)}%)", f"{total_with_vat:,.2f} €")

# ---------------------------------------------------------
# 1. Τοιχοποιία
# ---------------------------------------------------------
elif menu == "🧱 1. Τοιχοποιία & Υλικά":
    st.markdown('<div class="main-header">🧱 Υπολογισμός Τοιχοποιίας & Κοστολόγιο</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        length = st.number_input("Μήκος Τοίχου (m)", min_value=0.1, value=5.0, step=0.1, key="brick_len")
        height = st.number_input("Ύψος Τοίχου (m)", min_value=0.1, value=2.8, step=0.1, key="brick_height")
        openings = st.number_input("Εμβαδόν Ανοιγμάτων (sq.m)", min_value=0.0, value=2.0, key="brick_op")
    with col2:
        brick_type = st.selectbox("Τύπος Τούβλου", ["Μονό (9x19x19 cm)", "Διπλό (19x19x19 cm)", "Τσιμεντόλιθος"], key="brick_type_sel")
        waste = st.slider("Ποσοστό Φύρας (%)", 0, 15, 5, key="brick_waste")
        price_per_brick = st.number_input("Τιμή Μονάδος ανά Τούβλο (€)", min_value=0.0, value=0.45, step=0.05, key="p_brick")

    if st.button("Υπολογισμός Τοιχοποιίας & Κόστους", key="calc_bricks_btn"):
        area = max(0.0, (length * height) - openings)
        per_sqm = 25 if "Μονό" in brick_type else 50
        total_bricks = int(area * per_sqm * (1 + waste/100))
        mortar = area * 0.04
        cost = total_bricks * price_per_brick

        st.session_state['bricks_count'] = total_bricks
        st.session_state['mortar_vol'] = mortar
        st.session_state['brick_cost'] = cost

        st.markdown("---")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Καθαρό Εμβαδόν", f"{area:.2f} τ.μ.")
        c2.metric("Τούβλα (με φύρα)", f"{total_bricks} τμχ")
        c3.metric("Λάσπη Χτισίματος", f"{mortar:.2f} κ.μ.")
        c4.metric("Κόστος Τούβλων", f"{cost:.2f} €")
        st.success("✔ Τα αποτελέσματα και το κόστος αποθηκεύτηκαν!")

    add_photo_uploader("Σχέδιο / Φωτογραφία Τοίχου")

# ---------------------------------------------------------
# 2. Σκυρόδεμα
# ---------------------------------------------------------
elif menu == "📐 2. Σκυρόδεμα, Σενάζ & Ανώφλια":
    st.markdown('<div class="main-header">📐 Υπολογισμός Σκυροδέματος & Οικονομικά</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        l = st.number_input("Μήκος (m)", min_value=0.1, value=10.0, key="conc_l")
        w = st.number_input("Πλάτος/Πάχος (m)", min_value=0.05, value=0.20, key="conc_w")
        h = st.number_input("Ύψος/Βάθος (m)", min_value=0.05, value=0.20, key="conc_h")
    with col2:
        rebar = st.number_input("Αριθμός Βεργών Σιδήρου", min_value=1, value=4, key="conc_rebar")
        price_per_m3 = st.number_input("Τιμή Έτοιμου Μπετόν (€/κ.μ.)", min_value=0.0, value=95.0, step=5.0, key="p_conc")

    if st.button("Υπολογισμός Σκυροδέματος & Κόστους", key="calc_conc_btn"):
        vol = l * w * h
        rebar_len = l * rebar
        cost = vol * price_per_m3

        st.session_state['concrete_vol'] = vol
        st.session_state['rebar_len'] = rebar_len
        st.session_state['conc_cost'] = cost

        st.markdown("---")
        c1, c2, c3 = st.columns(3)
        c1.metric("Όγκος Μπετόν", f"{vol:.3f} κ.μ.")
        c2.metric("Συνολικό Μήκος Σιδήρου", f"{rebar_len:.1f} m")
        c3.metric("Κόστος Μπετόν", f"{cost:.2f} €")
        st.success("✔ Τα αποτελέσματα αποθηκεύτηκαν!")

    add_photo_uploader("Σχέδιο / Φωτογραφία Καλουπιού")

# ---------------------------------------------------------
# 3. Σοβάδες
# ---------------------------------------------------------
elif menu == "🧱 3. Σοβάδες & Επιχρίσματα":
    st.markdown('<div class="main-header">🧱 Υπολογισμός Σοβάδων & Κόστους</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        plaster_area = st.number_input("Επιφάνεια Σοβατίσματος (τ.μ.)", min_value=0.1, value=50.0, key="pl_area")
        thickness_mm = st.number_input("Μέσο Πάχος Σοβά (mm)", min_value=5, value=20, key="pl_thick")
    with col2:
        price_per_25kg = st.number_input("Τιμή Σακιού 25kg Έτοιμου Σοβά (€)", min_value=0.0, value=6.50, step=0.50, key="p_plaster")

    if st.button("Υπολογισμός Σοβά & Κόστους", key="calc_pl_btn"):
        ready_mix_kg = plaster_area * (thickness_mm * 1.5)
        bags_25kg = int(ready_mix_kg / 25) + 1
        cost = bags_25kg * price_per_25kg

        st.session_state['plaster_kg'] = ready_mix_kg
        st.session_state['plaster_bags'] = bags_25kg
        st.session_state['plaster_cost'] = cost

        st.markdown("---")
        c1, c2, c3 = st.columns(3)
        c1.metric("Απαιτούμενο Μίγμα", f"{ready_mix_kg:.0f} kg")
        c2.metric("Σακιά (25kg)", f"{bags_25kg} σακ.")
        c3.metric("Κόστος Υλικών Σοβά", f"{cost:.2f} €")
        st.success("✔ Τα αποτελέσματα αποθηκεύτηκαν!")

    add_photo_uploader("Φωτογραφία Επιφάνειας")

# ---------------------------------------------------------
# 4. Πλακάκια & Τσεκολατούρες
# ---------------------------------------------------------
elif menu == "🔳 4. Πλακάκια, Δάπεδα & Τσεκολατούρες":
    st.markdown('<div class="main-header">🔳 Υπολογισμός Πλακιδίων & Οικονομική Προσφορά</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        floor_area = st.number_input("Εμβαδόν Δαπέδου (τ.μ.)", min_value=0.1, value=30.0, key="fl_area")
        perimeter = st.number_input("Περίμετρος Χώρου (m)", min_value=0.5, value=22.0, key="fl_per")
        tile_w = st.number_input("Πλάτος Πλακιδίου (cm)", min_value=5, value=60, key="t_w")
        tile_h = st.number_input("Μήκος Πλακιδίου (cm)", min_value=5, value=60, key="t_h")
        price_per_sqm = st.number_input("Τιμή Πλακιδίου ανά τ.μ. (€)", min_value=0.0, value=18.50, step=1.0, key="p_tile_sqm")
    with col2:
        tile_waste = st.slider("Ποσοστό Φύρας (%)", 0, 20, 10, key="t_waste")
        joint_mm = st.selectbox("Πάχος Αρμού (mm)", [1.0, 2.0, 3.0, 4.0, 5.0], index=1, key="t_joint")
        has_skirting = st.checkbox("Υπολογισμός Τσεκολατούρων", value=True, key="t_skirt")
        price_per_glue = st.number_input("Τιμή Σακιού Κόλλας 25kg (€)", min_value=0.0, value=12.0, step=1.0, key="p_glue")

    if st.button("Υπολογισμός Πλακιδίων & Κόστους", key="calc_tiles_btn"):
        total_area_needed = floor_area * (1 + tile_waste/100)
        tile_area_sqm = (tile_w / 100) * (tile_h / 100)
        tiles_count = int(total_area_needed / tile_area_sqm)
        glue_bags = int((floor_area * 4) / 25) + 1
        
        skirting_tiles = 0
        if has_skirting:
            skirting_tiles = int(perimeter / (tile_h / 100)) + 1

        cost_tiles = total_area_needed * price_per_sqm
        cost_glue = glue_bags * price_per_glue
        total_cost = cost_tiles + cost_glue

        st.session_state['tiles_count'] = tiles_count
        st.session_state['tiles_sqm'] = total_area_needed
        st.session_state['tile_glue_bags'] = glue_bags
        st.session_state['skirting_tiles'] = skirting_tiles
        st.session_state['tiles_cost'] = total_cost

        st.markdown("---")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("τ.μ. Πλακιδίων (με φύρα)", f"{total_area_needed:.2f} τ.μ.")
        c2.metric("Πλακάκια Δαπέδου", f"{tiles_count} τμχ")
        c3.metric("Κόλλα (25kg)", f"{glue_bags} σακ.")
        c4.metric("Συνολικό Κόστος", f"{total_cost:.2f} €")
        st.success("✔ Τα αποτελέσματα αποθηκεύτηκαν!")

    add_photo_uploader("Σχέδιο / Φωτογραφία Πλακιδίων")

# ---------------------------------------------------------
# 5. Χρώματα
# ---------------------------------------------------------
elif menu == "🎨 5. Χρώματα & Βαφές":
    st.markdown('<div class="main-header">🎨 Υπολογισμός Βαφών & Κόστους</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        paint_area = st.number_input("Επιφάνεια Βαφής (τ.μ.)", min_value=0.1, value=80.0, key="p_area")
        coats = st.slider("Αριθμός Χεριών", 1, 4, 2, key="p_coats")
    with col2:
        coverage_per_liter = st.number_input("Απόδοση (τ.μ./L ανά χέρι)", min_value=5.0, value=11.0, key="p_cov")
        price_per_10l = st.number_input("Τιμή Δοχείου 10L (€)", min_value=0.0, value=45.0, step=5.0, key="p_paint_bucket")

    if st.button("Υπολογισμός Βαφής & Κόστους", key="calc_paint_btn"):
        total_liters = (paint_area * coats) / coverage_per_liter
        buckets_10l = int(total_liters / 10) + (1 if total_liters % 10 > 0 else 0)
        cost = buckets_10l * price_per_10l

        st.session_state['paint_liters'] = total_liters
        st.session_state['paint_buckets'] = buckets_10l
        st.session_state['paint_cost'] = cost

        st.markdown("---")
        c1, c2, c3 = st.columns(3)
        c1.metric("Συνολικά Λίτρα", f"{total_liters:.1f} L")
        c2.metric("Δοχεία (10L)", f"{buckets_10l} τμχ")
        c3.metric("Κόστος Χρωμάτων", f"{cost:.2f} €")
        st.success("✔ Τα αποτελέσματα αποθηκεύτηκαν!")

    add_photo_uploader("Φωτογραφία Βαφής")

# ---------------------------------------------------------
# 6. Μονώσεις
# ---------------------------------------------------------
elif menu == "🛡️ 6. Μονώσεις & Στεγάνωση":
    st.markdown('<div class="main-header">🛡️ Υπολογισμός Μονώσεων & Κόστους</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        insul_area = st.number_input("Επιφάνεια Μόνωσης (τ.μ.)", min_value=0.1, value=100.0, key="ins_area")
        insul_type = st.selectbox("Τύπος Μόνωσης", ["Θερμομόνωση (EPS/XPS)", "Στεγάνωση Ταράτσας (Ελαστομερές)", "Ασφαλτόπανο"], key="ins_type")
    with col2:
        price_unit = st.number_input("Τιμή Μονάδος (ανά τ.μ., kg ή ρολό) (€)", min_value=0.0, value=12.0, step=1.0, key="p_ins_unit")

    if st.button("Υπολογισμός Μόνωσης & Κόστους", key="calc_ins_btn"):
        st.markdown("---")
        if "Θερμομόνωση" in insul_type:
            total_insul_area = insul_area * 1.05
            cost = total_insul_area * price_unit
            st.session_state['insul_type_name'] = "Θερμομόνωση EPS/XPS"
            st.session_state['insul_result'] = f"{total_insul_area:.1f} τ.μ."
        elif "Στεγάνωση" in insul_type:
            total_kg = insul_area * 3 * 0.5
            cost = total_kg * price_unit
            st.session_state['insul_type_name'] = "Ελαστομερές Στεγανωτικό"
            st.session_state['insul_result'] = f"{total_kg:.1f} kg"
        else:
            total_asphalt = insul_area * 1.10
            rolls = int(total_asphalt / 10) + 1
            cost = rolls * price_unit
            st.session_state['insul_type_name'] = "Ασφαλτόπανο"
            st.session_state['insul_result'] = f"{rolls} ρολά"

        st.session_state['insul_cost'] = cost

        c1, c2 = st.columns(2)
        c1.metric("Ποσότητα Υλικού", st.session_state['insul_result'])
        c2.metric("Κόστος Μόνωσης", f"{cost:.2f} €")
        st.success("✔ Τα αποτελέσματα αποθηκεύτηκαν!")

    add_photo_uploader("Φωτογραφία Μόνωσης")

# ---------------------------------------------------------
# 7. Αναφορά & Προσφορά
# ---------------------------------------------------------
elif menu == "📄 7. Συγκεντρωτική Αναφορά & Προσφορά":
    st.markdown('<div class="main-header">📄 Οικονομική Προσφορά & Συγκεντρωτική Αναφορά</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Αυτόματη παραγωγή επαγγελματικού δελτίου προσφοράς και υλικών.</div>', unsafe_allow_html=True)

    project_name = st.session_state.get('global_project_name', 'Ανακαίνιση')
    company_name = st.session_state.get('global_company_name', 'Τεχνική Εταιρεία')
    client_name = st.session_state.get('global_client_name', 'Πελάτης')
    client_tax = st.session_state.get('global_client_tax', '-')
    vat_rate = st.session_state.get('global_vat', 24)

    notes = st.text_area("Γενικές Σημειώσεις Προσφοράς", "Οι τιμές επιβαρύνονται με τον νόμιμο ΦΠΑ. Ισχύς προσφοράς 30 ημέρες.", key="rep_notes_final")

    st.markdown("---")
    st.subheader("📋 Αναλυτικός Πίνακας Υλικών & Προϋπολογισμού")

    summary_data = []

    if "bricks_count" in st.session_state:
        summary_data.append({"Ενότητα": "1. Τοιχοποιία", "Περιγραφή": "Τούβλα (τεμ)", "Ποσότητα": f"{st.session_state['bricks_count']} τμχ", "Κόστος (€)": f"{st.session_state.get('brick_cost', 0):.2f}"})
    if "concrete_vol" in st.session_state:
        summary_data.append({"Ενότητα": "2. Σκυρόδεμα", "Περιγραφή": "Έτοιμο Μπετόν", "Ποσότητα": f"{st.session_state['concrete_vol']:.2f} κ.μ.", "Κόστος (€)": f"{st.session_state.get('conc_cost', 0):.2f}"})
    if "plaster_kg" in st.session_state:
        summary_data.append({"Ενότητα": "3. Σοβάδες", "Περιγραφή": "Έτοιμος Σοβάς", "Ποσότητα": f"{st.session_state.get('plaster_bags', 0)} σακ.", "Κόστος (€)": f"{st.session_state.get('plaster_cost', 0):.2f}"})
    if "tiles_count" in st.session_state:
        summary_data.append({"Ενότητα": "4. Πλακάκια", "Περιγραφή": "Πλακάκια & Κόλλες", "Ποσότητα": f"{st.session_state.get('tiles_sqm', 0):.2f} τ.μ.", "Κόστος (€)": f"{st.session_state.get('tiles_cost', 0):.2f}"})
    if "paint_liters" in st.session_state:
        summary_data.append({"Ενότητα": "5. Βαφές", "Περιγραφή": "Χρώματα", "Ποσότητα": f"{st.session_state.get('paint_buckets', 0)} δοχεία 10L", "Κόστος (€)": f"{st.session_state.get('paint_cost', 0):.2f}"})
    if "insul_result" in st.session_state:
        summary_data.append({"Ενότητα": "6. Μονώσεις", "Περιγραφή": st.session_state.get('insul_type_name', 'Μόνωση'), "Ποσότητα": st.session_state['insul_result'], "Κόστος (€)": f"{st.session_state.get('insul_cost', 0):.2f}"})

    if summary_data:
        df = pd.DataFrame(summary_data)
        st.table(df)

        total_net = sum(float(item["Κόστος (€)"]) for item in summary_data)
        total_vat = total_net * (vat_rate / 100)
        grand_total = total_net + total_vat

        st.markdown(f"""
        <div class="cost-card">
            <h4>💰 Οικονομική Σύνοψη Προσφοράς</h4>
            <p><b>Καθαρή Αξία Υλικών:</b> {total_net:,.2f} €</p>
            <p><b>ΦΠΑ ({vat_rate}%):</b> {total_vat:,.2f} €</p>
            <h3><b>ΓΕΝΙΚΟ ΣΥΝΟΛΟ: {grand_total:,.2f} €</b></h3>
        </div>
        """, unsafe_allow_html=True)

        text_report = f"""==================================================
ΟΙΚΟΝΟΜΙΚΗ ΠΡΟΣΦΟΡΑ & ΜΕΛΕΤΗ ΥΛΙΚΩΝ
==================================================
Εταιρεία: {company_name}
Έργο: {project_name}
Πελάτης: {client_name} (ΑΦΜ: {client_tax})
--------------------------------------------------
ΑΝΑΛΥΣΗ ΥΛΙΚΩΝ & ΚΟΣΤΟΥΣ:
"""
        for item in summary_data:
            text_report += f"- [{item['Ενότητα']}] {item['Περιγραφή']} | Ποσότητα: {item['Ποσότητα']} | Κόστος: {item['Κόστος (€)']} €\n"

        text_report += f"""--------------------------------------------------
Καθαρή Αξία: {total_net:,.2f} €
ΦΠΑ ({vat_rate}%): {total_vat:,.2f} €
ΣΥΝΟΛΙΚΟ ΚΟΣΤΟΣ: {grand_total:,.2f} €
--------------------------------------------------
ΣΗΜΕΙΩΣΕΙΣ:
{notes}
=================================================="""

        st.markdown("---")
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            st.download_button(
                label="📥 Λήψη Προσφοράς (.txt)",
                data=text_report,
                file_name=f"Prosfora_{project_name.replace(' ', '_')}.txt",
                mime="text/plain"
            )
        with col_btn2:
            csv_data = df.to_csv(index=False).encode('utf-8-sig')
            st.download_button(
                label="📊 Λήψη Πίνακα Προσφοράς (Excel / CSV)",
                data=csv_data,
                file_name=f"Prosfora_{project_name.replace(' ', '_')}.csv",
                mime="text/csv"
            )
    else:
        st.warning("⚠️ Δεν υπάρχουν ακόμα αποθηκευμένοι υπολογισμοί. Μεταβείτε στις ενότητες (1-6) και πατήστε 'Υπολογισμός'!")

    add_photo_uploader("Φωτογραφία / Σφραγίδα Έργου")