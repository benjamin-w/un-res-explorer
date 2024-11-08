import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO

<<<<<<< HEAD
st.title("UNGA Disarmament Resolution Tracker")
=======
st.title("UNGA Resolution Tracker")
>>>>>>> 9bf741d (initial commit)

@st.cache_data
def load_UN_database():
    # Replace this with your actual data loading code
<<<<<<< HEAD
    df =  pd.read_csv("disarmament_un_resolutions_position.csv")
=======
    df =  pd.read_csv("../data/2024-03-13_un_resolutions_positions.csv")
>>>>>>> 9bf741d (initial commit)
    return df

# Load the DataFrame (cached after the first load)
df = load_UN_database()

un_countries_iso_alpha3 = {
    "Afghanistan": "AFG",
    "Albania": "ALB",
    "Algeria": "DZA",
    "Andorra": "AND",
    "Angola": "AGO",
    "Antigua and Barbuda": "ATG",
    "Argentina": "ARG",
    "Armenia": "ARM",
    "Australia": "AUS",
    "Austria": "AUT",
    "Azerbaijan": "AZE",
    "Bahamas": "BHS",
    "Bahrain": "BHR",
    "Bangladesh": "BGD",
    "Barbados": "BRB",
    "Belarus": "BLR",
    "Belgium": "BEL",
    "Belize": "BLZ",
    "Benin": "BEN",
    "Bhutan": "BTN",
    "Bolivia": "BOL",
    "Bosnia and Herzegovina": "BIH",
    "Botswana": "BWA",
    "Brazil": "BRA",
    "Brunei Darussalam": "BRN",
    "Bulgaria": "BGR",
    "Burkina Faso": "BFA",
    "Burundi": "BDI",
    "Cabo Verde": "CPV",
    "Cambodia": "KHM",
    "Cameroon": "CMR",
    "Canada": "CAN",
    "Central African Republic": "CAF",
    "Chad": "TCD",
    "Chile": "CHL",
    "China": "CHN",
    "Colombia": "COL",
    "Comoros": "COM",
    "Congo (Congo-Brazzaville)": "COG",
    "Congo, Democratic Republic of the": "COD",
    "Costa Rica": "CRI",
    "Croatia": "HRV",
    "Cuba": "CUB",
    "Cyprus": "CYP",
    "Czechia (Czech Republic)": "CZE",
    "Denmark": "DNK",
    "Djibouti": "DJI",
    "Dominica": "DMA",
    "Dominican Republic": "DOM",
    "Ecuador": "ECU",
    "Egypt": "EGY",
    "El Salvador": "SLV",
    "Equatorial Guinea": "GNQ",
    "Eritrea": "ERI",
    "Estonia": "EST",
    "Eswatini (Swaziland)": "SWZ",
    "Ethiopia": "ETH",
    "Fiji": "FJI",
    "Finland": "FIN",
    "France": "FRA",
    "Gabon": "GAB",
    "Gambia": "GMB",
    "Georgia": "GEO",
    "Germany": "DEU",
    "Ghana": "GHA",
    "Greece": "GRC",
    "Grenada": "GRD",
    "Guatemala": "GTM",
    "Guinea": "GIN",
    "Guinea-Bissau": "GNB",
    "Guyana": "GUY",
    "Haiti": "HTI",
    "Honduras": "HND",
    "Hungary": "HUN",
    "Iceland": "ISL",
    "India": "IND",
    "Indonesia": "IDN",
    "Iran (Islamic Republic of)": "IRN",
    "Iraq": "IRQ",
    "Ireland": "IRL",
    "Israel": "ISR",
    "Italy": "ITA",
    "Jamaica": "JAM",
    "Japan": "JPN",
    "Jordan": "JOR",
    "Kazakhstan": "KAZ",
    "Kenya": "KEN",
    "Kiribati": "KIR",
    "Korea (Democratic People's Republic of)": "PRK",
    "Korea, Republic of": "KOR",
    "Kuwait": "KWT",
    "Kyrgyzstan": "KGZ",
    "Lao People's Democratic Republic": "LAO",
    "Latvia": "LVA",
    "Lebanon": "LBN",
    "Lesotho": "LSO",
    "Liberia": "LBR",
    "Libya": "LBY",
    "Liechtenstein": "LIE",
    "Lithuania": "LTU",
    "Luxembourg": "LUX",
    "Madagascar": "MDG",
    "Malawi": "MWI",
    "Malaysia": "MYS",
    "Maldives": "MDV",
    "Mali": "MLI",
    "Malta": "MLT",
    "Marshall Islands": "MHL",
    "Mauritania": "MRT",
    "Mauritius": "MUS",
    "Mexico": "MEX",
    "Micronesia (Federated States of)": "FSM",
    "Monaco": "MCO",
    "Mongolia": "MNG",
    "Montenegro": "MNE",
    "Morocco": "MAR",
    "Mozambique": "MOZ",
    "Myanmar": "MMR",
    "Namibia": "NAM",
    "Nauru": "NRU",
    "Nepal": "NPL",
    "Netherlands": "NLD",
    "New Zealand": "NZL",
    "Nicaragua": "NIC",
    "Niger": "NER",
    "Nigeria": "NGA",
    "North Macedonia": "MKD",
    "Norway": "NOR",
    "Oman": "OMN",
    "Pakistan": "PAK",
    "Palau": "PLW",
    "Panama": "PAN",
    "Papua New Guinea": "PNG",
    "Paraguay": "PRY",
    "Peru": "PER",
    "Philippines": "PHL",
    "Poland": "POL",
    "Portugal": "PRT",
    "Qatar": "QAT",
    "Romania": "ROU",
    "Russian Federation": "RUS",
    "Rwanda": "RWA",
    "Saint Kitts and Nevis": "KNA",
    "Saint Lucia": "LCA",
    "Saint Vincent and the Grenadines": "VCT",
    "Samoa": "WSM",
    "San Marino": "SMR",
    "Sao Tome and Principe": "STP",
    "Saudi Arabia": "SAU",
    "Senegal": "SEN",
    "Serbia": "SRB",
    "Seychelles": "SYC",
    "Sierra Leone": "SLE",
    "Singapore": "SGP",
    "Slovakia": "SVK",
    "Slovenia": "SVN",
    "Solomon Islands": "SLB",
    "Somalia": "SOM",
    "South Africa": "ZAF",
    "South Sudan": "SSD",
    "Spain": "ESP",
    "Sri Lanka": "LKA",
    "Sudan": "SDN",
    "Suriname": "SUR",
    "Sweden": "SWE",
    "Switzerland": "CHE",
    "Syrian Arab Republic": "SYR",
    "Tajikistan": "TJK",
    "Thailand": "THA",
    "Timor-Leste": "TLS",
    "Togo": "TGO",
    "Tonga": "TON",
    "Trinidad and Tobago": "TTO",
    "Tunisia": "TUN",
    "Turkey": "TUR",
    "Turkmenistan": "TKM",
    "Tuvalu": "TUV",
    "Uganda": "UGA",
    "Ukraine": "UKR",
    "United Arab Emirates": "ARE",
    "United Kingdom of Great Britain and Northern Ireland": "GBR",
    "United States of America": "USA",
    "Uruguay": "URY",
    "Uzbekistan": "UZB",
    "Vanuatu": "VUT",
    "Venezuela (Bolivarian Republic of)": "VEN",
    "Viet Nam": "VNM",
    "Yemen": "YEM",
    "Zambia": "ZMB",
    "Zimbabwe": "ZWE"
}

years_string = [str(year) for year in np.arange(2023,1993,-1)]

un_topic_index = {"Disarmament" : '129'}

country_options = st.multiselect(
    "Pick countries to compare",
    un_countries_iso_alpha3,
    [],
)

year_option = st.selectbox(
    "Pick year",
    years_string
)

topic_option = st.selectbox(
    "Pick topic",
    un_topic_index
)

country_string = [str(un_countries_iso_alpha3[countries]) for countries in country_options]

query_string = "iso_alpha3_code in @country_string & year == "+year_option+" & main_category_"+un_topic_index[topic_option]+" == 1"

df_filtered = df.query(query_string)[["title", "iso_alpha3_code", "yes","no","abstentions","position"]].drop_duplicates(subset=['title', 'iso_alpha3_code'])
df_pivoted = df_filtered.pivot(index='title', columns=['iso_alpha3_code'], values='position').reset_index()
un_votes = df_filtered[['title', 'yes', 'no','abstentions']].drop_duplicates(subset=['title']).reset_index(drop=True)
df_merged = pd.merge(df_pivoted, un_votes, on='title', how='left')

st.dataframe(df_merged)

# write xlsx file
def color_cells(val):
    if val == "y":
        color = 'background-color: lightgreen'
    elif val == "n":
        color = 'background-color: lightcoral'
    elif val == "a":
        color = 'background-color: LemonChiffon'
    else:
        color = ''
    return color


def create_excel_file(dframe):
    output = BytesIO()
    styled_df = dframe.style.applymap(color_cells, subset=country_string)
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        styled_df.to_excel(writer, index=False, sheet_name='Vote Records')
    output.seek(0)  # Rewind the buffer
    return output

# Create the Excel file
excel_file = create_excel_file(df_merged)

if excel_file:
    # Create a download button in Streamlit
    st.download_button(
        label="Download voting history as Excel",
        data=excel_file,
        file_name="voting_record_"+'_'.join(country_string)+"_year_"+year_option+".xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
else:
    st.write("Failed to create Excel file.")
