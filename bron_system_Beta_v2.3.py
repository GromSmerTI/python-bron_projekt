# Ruumide broneerimise süsteem
# Andreev Vyacheslav JPIT24

# Moodulid
import streamlit as st
import mysql.connector
from datetime import datetime, timedelta
import hashlib
import pandas as pd

# Andmebaasi ühendamine
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bron_projekt",
    port=3306
)

# Vanade broneeringute kustutamine
cursor = conn.cursor()
cursor.execute("DELETE FROM cabinets WHERE Date < CURDATE() - INTERVAL 1 MONTH")
conn.commit()

# Lehekülje konfiguratsioonide seadistamine
st.set_page_config(
    page_title="Broneerimise süsteem",
    page_icon="🏢"
)

# Paroolide dekrüpteerimise funktsioon
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Kasutaja tegeliku nime saamise funktsioon
def get_real_name(username: str) -> str:
    cursor.execute("SELECT real_name FROM users WHERE nickname = %s", (username,))
    result = cursor.fetchone()
    return result[0] if result else username

# Klassiruumide ja õppeainete nimekirjad
cabinets_list = ["B101", "B102", "B103", "B104", "B105", "B110", "B111", "B112", "C104", "C105", "C111", "C112", "C113", "C114", "C204", "C205", "C211", "C212", "C213", "C214", "C304", "C305", "C311", "C312", "C313", "C314", "F239", "F240", "F243", "F245", "E101", "E102", "E103", "E104", "E105", "E106", "E107", "E108", "E109", "E110", "E111", "E112", "E201", "E202", "E203", "E204", "E209", "E210", "Laboratoorium - E1", "Laboratoorium - E2", "Salong", "Spordisaal", "Väljaspool kooli"]

ruhm_list = ["JPIT24", "JPIT23", "JPIT22", "JPITE21", "JPTV24", "JPTV23", "JPTV22", "JPTV21", "JPAS24", "JPAS23", "JPAS22", "JPEPE24", "JPEPE23", "JPLT24", "JPLT23", "JPLT22", "JPLB24", "JPLB23", "JPLB22", "JPJUE24", "JPJUE23", "JPJUE22", "Rühm puudub"]

eri_list = ["Grupijuhendaja tund", "Mentorluse tund", "Tuutoruse tund", "Infotund"]

aleksander_pulver_list = ["Programmerimise alused", "IT-valdkonna alusteadmised", "IT-korraldus", "Digioskuste kuiundamine", "Portfoolio koostamine", "Portfoolio koostamine. Fotod ja töötlemine", "Praktika", "Kutseeksam", "Laboritööd", "Konsultatsioon"]

nadezda_pahka_list = ["Abiõpetaja tund (eesti keel)", "Abiõpetaja tund (KOHUSTUSLIK)", "Konsultatsioon"]

tiit_raik_list = ["Küberturvalisus", "Haldustegevuste automatiseerimine", "Pilveteenused", "Majutuskeskkonna riistvara", "Linux/BSD operatsioonisüsteemid", "Praktika", "Laboritööd", "Lõputöö", "Konsultatsioon"]

vladislav_mikson_list = ["Digivahendite kasutamine töös", "Labori dokumentatsioon. IT", "Erialane infotehnoloogia. JOONISTE VORMISTAMINE JA TÄIENDAMINE", "Erialane infotehnoloogia", "Hooneautomaatika paigaldamine ja käit. Erialane joonestamine", "Infoturbe haldamine", "Linux/BSD operatsioonisüsteemid", "CAD programmid", "Sissejuhatus eriala õpingutesse", "Programmeerimise alused", "IT-korralduse alused", "Keskkonnahoid. IT", "1.IT", "OPERATSIOONISÜSTEEMID", "Õpi- ja digioskuste kujundamine. IT", "Lõputöö seminar ja ettevalmistus kutseeksamiks", "Tööjaamade keskne haldamine. Mobiiliseadmete turvalisus.Kaitse rünnakute eest.", "Konsultatsioon"]

aleksandr_vainokivi_list = ["Arvutivõrgud", "Klientseadmete haldus", "Rakendusserverid", "Praktika", "Laboritööd", "Konsultatsioon"]

heidi_edela_list = ["Õpitee ja töö muutuvas keskkonnas", "Õpitee ja töö muutuvas keskkonnas. Majandus ja ettevõtlus", "Õpitee ja töö muutuvas keskkonnas 3 (Projekt); Õpitee ja töö muutuvas keskkonnas 4 (Karjääritee ja kutsealase areng)", "Õpitee", "Ettevõtluse alused", "Majanduse ja ettevõtluse alused", "Karjääritee ja kutsealase areng", "MAJANDUSE ALUSED", "Konsultatsioon"]

marina_pavlova_list = ["Erialane võõrkeel", "Erialane inglise keel", "Erialane võõrkeel. Dokumentatsiooni koostamine", "Hoone automaatika– ja väikepingeseadmete paigaldamine. Lõimitud inglise keel", "Erialane inglise keel. Lao klienditeenindus", "Labori- töökorraldus, tehnika, ohutushoid. Inglise keel", "Masinaehituse tehnilised alused / Lõimitud inglise keel", "Käsikaarkeevitus. Lõimitud inglise keel", "Logistika alused. Inglise keel", "Konsultatsioon"]

viivi_treier_list = ["Eesti keel teise keelena", "Eesti keele C1 kursused", "Eesti keele täiendav õppe", "Keel ja kirjandus", "Käsikaarkeevitus. Lõimitud eesti keel", "Eesti keele põhiteadmisi ühtlustav moodul", "Konsultatsioon"]

alevtina_serova_list = ["Erialane võõrkeel", "Võõrkeel", "Erialane inglise keel. Lao klienditeenindus", "Inglise keel", "Keskkonnahoid. Lõimitud inglise keel", "Erialane võõrkeel. Dokumentatsiooni koostamine", "Käsikaarkeevitus. Lõimitud inglise keel", "Instrumentaalanalüüs ja proovide võtmine. Inglise keel", "Konsultatsioon"]

urmas_treier_list = ["Riigikaitse", "Kehaline kasvatus", "Metallitööde alused. Lõimitud kehaline kasvatus", "Instrumentaalanalüüs ja proovide võtmine. Lõimitud kehaline kasvatus", "Konsultatsioon"]

jaanek_pahka_list = ["Ajalugu", "Ühiskonnaõpetus", "Lõimitud ajalugu, inimgeograafia, ühiskonnaõpetus", "Konsultatsioon"]

ilia_bogatyrev_list = ["Matemaatika", "Füüsika", "Poolautomaatkeevitus / Lõimitud füüsika", "Erinevatest jahudest tainatoodete valmistamine. Lõimitud matemaatika", "Käsikaarkeevitus. Lõimitud füüsika", "Laotehnoloogiad ja -seadmed Matemaatika", "Konsultatsioon"]

oksana_pavelkovits_list = ["Matemaatika", "Hoone elektripaigaldiste ehitamine. Lõimitud füüsika", "Üldharidus. Reaalained", "Juuste värvitöötlus. Lõimitud matemaatika", "Füüsika", "Matemaatika põhikooli teadmiste ühtlustav moodul", "Logistika alused. Matemaatika", "Soengukujundus. Lõimitud matemaatika", "Matemaatika ühtlustav moodul", "Konsultatsioon"]

tatjana_kippr_list = ["Füüsika", "Matemaatika", "Täiendav matemaatika", "Lõimitud füüsika", "Füüsika.Laotehnoloogiad ja -seadmed", "Konsultatsioon"]

anna_torn_list = ["Keemia. Kaupade hoiustamine ja inventeerimine", "Keemia", "Keemia. Kauba väljastamine ja transport", "Bioloogia, keemia", "Metallitööde alused. Lõimitud keemia ja bioloogia", "Bioloogia", "Lõimitud loodusained", "Konsultatsioon"]

konstantin_malinovski_list = ["Tootmisautomaatika paigaldamine ja käit. PLC, tootmiskontroll", "Automaatiku alusteadmised. Loogika ja digitaal tehnika", "Tootmisautomaatika paigaldamine ja käit. Pneumo- ja Hüdroautomaatika, PLC", "Automaatiku alusteadmised. Pneumaatika, hüdraulika", "Konsultatsioon"]

tarvo_seljamae_list = ["Hoone elektripaigaldiste ehitamine. Kõrgustööd", "Tootmisautomaatika paigaldamine ja käit. Automaatjuhtimissüsteemid", "Elektroonika", "Hooneautomaatika paigaldamine ja käit. PLC", "Rakenduselektroonika ja automaatika", "Lukksepatööd", "Robootika", "Automaatiku alusteadmised. Automaatika alused", "Rakenduselektroonika ja automaatika. Automaatika alused", "Konsultatsioon"]

valeri_bostrov_list = ["Materjalide peale- ja mahalaadimine, ladustamine ja paigaldamine", "Tõstukid, nende hooldus ja juhtimine", "Materjalide peale- ja mahalaadimine, ladustamine ja paigaldamine", "Hoone elektripaigaldiste ehitamine. Kõrgustööd", "Automaatikaseadmete ja -süsteemide käit. Lukksepatööd", "Tõstukid, nende hooldus ja juhtimine", "Lukksepatööd", "Mehhatrooniku alusteadmised. Mehaanika alused", "Mehhatroonikaseadmete ja alamsüsteemide koostamine ja paigaldamine. Masinalõiketööd", "Laotehnoloogiad ja seadmed", "Grupijuhendaja tund", "Konsultatsioon"]

anna_pantelejeva_list = ["Klienditeeninduse praktilised tööd", "Soengu kujundamine", "Juuste värvimine", "Konsultatsioon"]

natalia_turilova_list = ["Klienditeeninduse praktilised tööd", "Pidulikud soengud", "Juuste värvitöötlus", "Soengukujundus", "Juuste struktuuri püsimuutmine", "Konsultatsioon"]

olga_varunina_list = ["Inimeseõpetus", "Keel ja kirjandus", "Lõimitud keel ja kirjandus", "Kodulugu", "Üldharidus. Humanitaarained", "Konsultatsioon"]

inga_lazarenko_list = ["Instrumentaalanalüüs ja proovide võtmine", "Mikrobioloogia analüüsid", "Anorgaaniline süntees", "Keskkonnahoid", "Labori dokumentatsioon", "Keskkonnahoid. Kemikaalide ohutu käitlemine", "Praktika", "Konsultatsioon"]

svetlana_avdejeva_list = ["Labori akrediteerimine ja kvaliteedijuhtimine", "Laboriseadmed ja töövahendid", "Orgaaniline süntees", "Instrumentaalanalüüs ja proovide võtmine. Tehniline analüüs", "Erialane keemia ja keemiline süntees", "Labori- töökorraldus, tehnika", "Kutseeksam", "Konsultatsioon"]

maarika_rummel_list = ["Eesti keel teise keelena", "Labori- töökorraldus, tehnika, ohutushoid. Lõimitud eesti keel", "Eesti keele täiendav õppe", "Erialane soome keel", "Keel ja kirjandus", "Keskkonnahoid. Lõimitud eesti keel", "Eesti keele põhiteadmisi ühtlustav moodul", "Toitlustamise valdkonna ja õpingute alused", "Toiduainetöötluse valdkonna alused", "Konsultatsioon"]

irina_leppik_list = ["Hoone elektripaigaldiste ehitamine. Materjaliõpetus. Ehituskonstruktsioonid ja -materjalid", "Erialane keemia ja keemiline süntees. Lõimitud füüsika", "Keemiaseadmete ja -tehnoloogia põhimõtted", "Automaatikaseadmete ja -süsteemide paigaldamine. Tehniline dokumentatsioon", "Sisetööde elektriku alusteadmised. Joonestamine", "Lukksepatööde teooria", "Ohutushoid", "Labori- töökorraldus, tehnika, ohutushoid. Sissejuhatus. Ohutushoid", "Materjaliõpetus", "Konsultatsioon"]

juri_melnikov_list = ["ARVUTIVÕRKUDE ALUSED", "Hooneautomaatika paigaldamine ja käit. Programmeerimine", "Programmeerimine II", "Pilverakendused", "Lõputöö", "Konsultatsioon"]

inna_dokutsajeva_list = ["Infotehnoloogia juhtimine ja rakendamine organisatsioonides", "IT juhtimine ja rakendamine organisatsioonides", "Tarkvarasüsteemide testimine", "Mobiilirakendused", "Mobiilirakenduse loomine", "Mobiilirakenduse loomise loogika ja protsess", "Õpitee ja töö muutuvas keskkonnas - Projekt", "Lõputöö", "Konsultatsioon"]

larissa_lavrentjeva_list = ["Karjääritee ja kutsealase areng", "Õpitee ja töö muutuvas keskkonnas", "Karjäär. Majandus", "Vene keel (ER)", "Kogukonnaprojekti teostamine", "Karjäär. Töökeskkond ja esmaabi", "Majandus ja ettevõtlus", "Majanduse ja ettevõtluse alused", "Kutsevaliku alused. Töötervishoid", "Õpitee", "Gruppijuhendaja tund", "Konsultatsioon"]

jelena_olikainen_list = ["Digioskuste kujundamine", "Arvutiõpetus", "IT", "IT valdkonna alusteadmised", "Excel, matemaatika", "Veebikujundus ja internetiturundus", "Andmebaasisüsteemide alused", "Märgendikeeledja stiililehed HTML, CSS. Seadmele kohanduvad", "Kasutajaliidese disain", "Lõputöö seminar ja ettevalmistus kutseeksamiks", "Lõputöö", "Konsultatsioon"]

olga_popova_list = ["Tarkvara arendusmeetodid", "Lõputöö seminar", "Veebiprogrammeerimine", "Hajusrakenduste alused", "Tarkvara arendusprotsess", "Veebirakenduste loomise alused", "Agiilsed tarkvaraarenduse metoodikad", "Konsultatsioon"]

jelena_kuzmina_list = ["Andmebaasisüsteemid", "Programmeerimise alused", "IT valdkonna alusteadmised. Ressursivajadus. Rakendustarkvara", "Lõputöö seminar", "Konsultatsioon"]

merili_kivimaa_list = ["Logistika- ja majandustarkvara. Laoarvestustarkvara", "Logistika e-kaubanduses", "Klienditeenindust mõjutavad faktorid. Pretensioonid ja reklamatsioonid logistikas.Toote ja teenuse kvaliteet", "Lao klienditeenindus.Tellimuste vastuvõtmine ja töötlemine", "Pakendid ja liigitus", "Hoiukohtade hooldamine. Puhtuse- ja hügieenireeglid. Lao korrashoid", "Riskid logistikas", "Klienditeeninduse korraldamine", "Inventuur", "Tabelitöötlus ja arvutused Excel ́is jätkukursus", "Erialane eesti keel", "Konsultatsioon"]

# Spetsialiseerumise sõnastik
subject_access = {
    "aleksander_pulver": aleksander_pulver_list,
    "tiit_raik": tiit_raik_list,
    "vladislav_mikson": vladislav_mikson_list,
    "aleksandr_vainokivi": aleksandr_vainokivi_list,
    "urmas_treier": urmas_treier_list,
    "heidi_edela": heidi_edela_list,
    "marina_pavlova": marina_pavlova_list,
    "nadezda_pahka": nadezda_pahka_list,
    "viivi_treier": viivi_treier_list,
    "alevtina_serova": alevtina_serova_list,
    "ilia_bogatyrev": ilia_bogatyrev_list,
    "tatjana_kippr": tatjana_kippr_list,
    "oksana_pavelkovits": oksana_pavelkovits_list,
    "anna_torn": anna_torn_list,
    "jaanek_pahka": jaanek_pahka_list,
    "konstantin_malinovski": konstantin_malinovski_list,
    "tarvo_seljamae": tarvo_seljamae_list,
    "valeri_bostrov": valeri_bostrov_list,
    "anna_pantelejeva": anna_pantelejeva_list,
    "natalia_turilova": natalia_turilova_list,
    "olga_varunina": olga_varunina_list,
    "inga_lazarenko": inga_lazarenko_list,
    "svetlana_avdejeva": svetlana_avdejeva_list,
    "maarika_rummel": maarika_rummel_list,
    "irina_leppik": irina_leppik_list,
    "juri_melnikov": juri_melnikov_list,
    "inna_dokutsajeva": inna_dokutsajeva_list,
    "larissa_lavrentjeva": larissa_lavrentjeva_list,
    "jelena_olikainen": jelena_olikainen_list,
    "olga_popova": olga_popova_list,
    "jelena_kuzmina": jelena_kuzmina_list,
    "merili_kivimaa": merili_kivimaa_list,
    "eri": eri_list
}

if "start" not in st.session_state:
    st.session_state["start"] = False

# Tervitusekraan
if not st.session_state["start"]:
    st.title("Ruumide broneerimise süsteem")
    st.write("See on süsteem õpperuumide broneerimiseks. See võimaldab teil vaadata hõivatud õpperuume, broneerida neid või kustutada broneeritud õpperuume.")
    st.write("Iga kasutaja saab broneeritud õpperuume vaadata. Ainult volitatud kasutajad saavad broneeringuid lisada või kustutada. Igal õpetajal on oma kasutajanimi ja parool ning nimekiri õppeainetest, mida ta saab broneerida.")
    st.write("Täna tehtud broneeringud on märgitud rohelise värviga. Homme tehtud broneeringud on märgitud kollase värviga. Sinise värviga on märgitud broneeringud, mille puhul on projekt kaitstud. Kõik broneeringud, mille tähtaeg on möödunud kuu aega tagasi, kustutatakse automaatselt.")
    st.markdown("""<div style="position: fixed; bottom: 10px; right: 10px; text-align: right; font-size: 12px; color: white; text-shadow: 0 0 5px #0f0, 0 0 10px #66ff66;"> <p>Valmistanud Vyacheslav Andreev</p></div>""", unsafe_allow_html=True)
    
    if st.button("Alusta programmi"):
        st.session_state["start"] = True
        st.rerun()
else:
    # Põhimenüü
    menu = st.sidebar.selectbox("Vali toiming", ["Vaata ruume", "Broneeri ruum", "Eemalda broneering"])
    side_text = st.sidebar.markdown("""<div style="position: fixed; bottom: 15px; left: 7%; text-align: left; font-size: 12px; color: white; text-shadow: 0 0 5px #ed4040, 0 0 10px #ed4040;"> <p>Jõhvi 2025</p></div>""", unsafe_allow_html=True)
    
    # Kasutaja sisselogimine/väljalogimine
    if "user" in st.session_state:
        if st.sidebar.button("Logi välja"):
            del st.session_state["user"]
            del st.session_state["prof"]
            st.rerun()
        real_name = get_real_name(st.session_state["user"])
        st.sidebar.success(f"Sisse logitud: {real_name}")
    else:
        if st.sidebar.button("Logi sisse"):
            st.session_state["login_form"] = True
        
        if st.session_state.get("login_form", False):
            with st.sidebar.form("Login Form"):
                st.subheader("Logi sisse")
                username = st.text_input("Kasutajanimi")
                password = st.text_input("Salasõna", type="password")
                
                if st.form_submit_button("Logi sisse"):
                    hashed_password = hash_password(password)
                    cursor.execute("SELECT * FROM users WHERE nickname = %s AND user_pass = %s", (username, hashed_password))
                    user = cursor.fetchone()
                    if user:
                        st.success(f"Tere tulemast, {user[3]}!")
                        st.session_state["user"] = username
                        st.session_state["prof"] = user[4]
                        st.session_state["login_form"] = False
                        st.rerun()
                    else:
                        st.error("Vale kasutajanimi või parool")

                if st.form_submit_button("Katkesta"):
                    st.session_state["login_form"] = False
                    st.rerun()

    # Ruumide vaatamine
    if menu == "Vaata ruume":
        st.subheader("Ruumide broneeringud")
        
        # Ruumi valik
        selected_cab = st.selectbox("Valige ruum", cabinets_list)
        
        # Broneeringute pärimine andmebaasist
        cursor.execute("""SELECT DATE_FORMAT(c.Date, '%d.%m.%Y') as Kuupäev, TIME_FORMAT(c.Time, '%H:%i') as Algus, TIME_FORMAT(c.Time_end, '%H:%i') as Lõpp, c.Subject as Õppeaine, u.real_name as Õpetaja, c.Grupp as Rühm, c.IsDefense FROM cabinets c JOIN users u ON c.`Reservation (name)` = u.nickname WHERE c.Cabinet = %s AND c.Date >= CURDATE() ORDER BY c.Date, c.Time""", (selected_cab,))
        reservations = cursor.fetchall()
        
        if reservations:
            # Tabel broneeringutega
            df_full = pd.DataFrame(reservations, columns=["Kuupäev", "Algus", "Lõpp", "Õppeaine", "Õpetaja", "Rühm", "IsDefense"])
            df = df_full.drop(columns=["IsDefense"])
            today_str = datetime.today().strftime("%d.%m.%Y")
            tomorrow_str = (datetime.today() + timedelta(days=1)).strftime("%d.%m.%Y")

            # Nullida indeks, mida ei näidata tabelis
            df.reset_index(drop = True, inplace = True)
            df_full.reset_index(drop=True, inplace=True)

            # Funktsioon tänapäeva ja homse kirjete esiletõstmiseks
            def highlight_days(row):
                if df_full.loc[row.name, 'IsDefense'] == 1:
                    return ['background-color: #80caff' for _ in row]  # Sinine
                elif row['Kuupäev'] == today_str:
                    return ['background-color: #5e9164' for _ in row]  # Rohaline
                elif row['Kuupäev'] == tomorrow_str:
                    return ['background-color: #b2b804' for _ in row]  # Kollane
                else:
                    return ['' for _ in row]

            styled_df = df.style.apply(highlight_days, axis=1)

            # Kuvada stiliseeritud tabel ilma indeksita ja automaatse laiusega
            st.dataframe(styled_df, use_container_width=True, hide_index=True)
            
        else:
            st.success(f"Ruum {selected_cab} on vaba kõigile tulevastele kuupäevadele!")

    # Ruumi broneerimine
    elif menu == "Broneeri ruum":
        if "user" not in st.session_state:
            st.warning("Palun logige sisse enne broneerimist.")
        else:
            st.subheader("Broneeri ruum")
            
            # Kuupäeva valik
            selected_date = st.date_input("Valige kuupäev", datetime.now())
            is_defense = st.checkbox("Projekti kaitsmine")
            
            # Kontroll, kas kuupäev on minevikus
            if selected_date < datetime.now().date():
                st.error("Valitud kuupäev on minevikus. Palun valige tuleviku kuupäev.")
            else:
                # Ruumi valik
                cab = st.selectbox("Valige ruum", cabinets_list)
                
                # Õppeainete filtreerimine kasutaja õiguste järgi
                prof_raw = st.session_state.get("prof", "")
                prof_list = [p.strip() for p in prof_raw.split(",")]
                filtered_subjects = []
                
                for prof in prof_list:
                    filtered_subjects.extend(subject_access.get(prof, []))
                
                filtered_subjects = sorted(set(filtered_subjects))
                
                if not filtered_subjects:
                    st.warning("Teie kasutajakontol puuduvad õigused õppeainete broneerimiseks.")
                else:
                    subject = st.selectbox("Valige õppeaine", filtered_subjects)
                    grupp = st.selectbox("Valige õpperühm", ruhm_list)
                    
                    # Aja valik
                    col1, col2 = st.columns(2)
                    with col1:
                        start_time = st.time_input("Algusaeg", step=900)
                    with col2:
                        end_time = st.time_input("Lõpuaeg", step=900)
                    
                    # Aja korrektuse kontroll
                    if start_time >= end_time:
                        st.error("Lõpuaeg peab olema hilisem kui algusaeg!")
                    else:
                        # Ruumi kättesaadavuse kontroll
                        cursor.execute("""SELECT TIME_FORMAT(Time, '%H:%i'), TIME_FORMAT(Time_end, '%H:%i') FROM cabinets WHERE Cabinet = %s AND Date = %s AND ((Time < %s AND Time_end > %s) OR (Time >= %s AND Time < %s))""", (cab, selected_date.strftime('%Y-%m-%d'), end_time.strftime('%H:%M'), start_time.strftime('%H:%M'), start_time.strftime('%H:%M'), end_time.strftime('%H:%M')))
                        conflicts = cursor.fetchall()
                        
                        if conflicts:
                            st.error("Valitud ajavahemik on juba broneeritud:")
                            for conflict in conflicts:
                                st.write(f"{conflict[0]} - {conflict[1]}")
                        else:
                            if st.button("Kinnita broneering"):
                                formatted_date = selected_date.strftime('%Y.%m.%d')
                                cursor.execute("""INSERT INTO cabinets (Cabinet, `Reservation (name)`, Subject, Time, Time_end, Date, Grupp, IsDefense) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", (cab, st.session_state["user"], subject, start_time.strftime('%H:%M'), end_time.strftime('%H:%M'), formatted_date, grupp, int(is_defense)))
                                conn.commit()
                                st.success(f"{grupp} — õpperuum {cab} on reserveeritud {formatted_date} "f"kell {start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')}")

    # Broneeringu eemaldamine
    elif menu == "Eemalda broneering":
        if "user" not in st.session_state:
            st.warning("Palun logige sisse enne broneeringu eemaldamist.")
        else:
            st.subheader("Eemalda broneering")
            
            # Ruumi valik
            selected_cab = st.selectbox("Valige ruum", cabinets_list)
            
            # Kasutaja broneeringute pärimine
            cursor.execute("""SELECT DATE_FORMAT(c.Date, '%d.%m.%Y') as Kuupäev, TIME_FORMAT(c.Time, '%H:%i') as Algus, TIME_FORMAT(c.Time_end, '%H:%i') as Lõpp, c.Subject as Õppeaine, c.Grupp as Rühm, c.ID FROM cabinets c WHERE c.Cabinet = %s AND c.Date >= CURDATE() AND c.`Reservation (name)` = %s ORDER BY c.Date, c.Time""", (selected_cab, st.session_state["user"]))
            reservations = cursor.fetchall()
            
            if reservations:
                st.write(f"Teie broneeringud ruumile {selected_cab}:")
                
                # Valikuvariandid
                options = [f"{res[0]} {res[1]}-{res[2]}: {res[3]} ({res[4]})" for res in reservations]
                selected = st.selectbox("Valige broneering", options)
                
                if st.button("Eemalda broneering"):
                    # Broneeringu ID leidmine
                    index = options.index(selected)
                    reservation_id = reservations[index][5]
                    
                    # Broneeringu eemaldamine
                    cursor.execute("DELETE FROM cabinets WHERE ID = %s", (reservation_id,))
                    conn.commit()
                    st.success("Broneering on edukalt eemaldatud!")
                    st.rerun()
            else:
                st.success("Teil pole broneeritud ruume.")