import streamlit as st
import os


def load_data(patient_index):
    # Load anamnesis file
    anamnesis_file_path = (
        f"./elaborazione/nota_clinica/anamnesi_paziente_{patient_index}.txt"
    )
    if os.path.exists(anamnesis_file_path):
        with open(anamnesis_file_path, "r") as file:
            anamnesis_data = file.read()
    else:
        anamnesis_data = "Anamnesis data not found for selected patient."

    # Load results
    results_file_path = "./elaborazione/results.txt"
    if os.path.exists(results_file_path):
        with open(results_file_path, "r") as file:
            results_data = file.read()
    else:
        results_data = "Results data not found."

    # Load and display the three most pertinent document parts
    docs_file_path = "./elaborazione/parti_maggiore_attinenza.txt"
    if os.path.exists(docs_file_path):
        with open(docs_file_path, "r") as file:
            docs_data = file.read()
    else:
        docs_data = "Document parts data not found."

    return anamnesis_data, results_data, docs_data


def main():
    st.title("Medical Data Analysis App")

    # Dropdown for patient selection
    patient_number = st.selectbox("Select Patient Number:", list(range(1, 101)))

    # Button to load data
    if st.button("Load Data"):
        anamnesis_data, results_data, docs_data = load_data(patient_number)

        # Text area for displaying anamnesis file
        st.subheader("Anamnesis:")
        st.text_area("Anamnesis Text", value=anamnesis_data, height=200)

        # Text area for displaying results
        st.subheader("Results:")
        st.text_area("Results Text", value=results_data, height=200)

        # Text area for displaying top 3 pertinent docs
        st.subheader("Top 3 Pertinent Documents:")
        st.text_area("Documents Text", value=docs_data, height=200)


if __name__ == "__main__":
    main()
