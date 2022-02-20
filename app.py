import streamlit as st

from utils import Experience, Qualification


def init_session_state():
    init_state = {"skills": [], "experiences": [], "qualifications": []}
    for key, value in init_state.items():
        if key not in st.session_state:
            st.session_state[key] = value


def update_skills():
    st.session_state.skills = [
        skill.strip() for skill in st.session_state.skill.split(",")
    ]


def add_experience():
    experience = Experience(
        job_title=st.session_state["experience_job_title"],
        company=st.session_state["experience_company"],
        summary=st.session_state["experience_summary"],
        start_date=st.session_state["experience_start_date"],
        end_date=st.session_state["experience_end_date"],
    )
    st.session_state.experiences += experience


def add_qualification():
    qualification = Qualification(
        name=st.session_state["qualification_name"],
        issuing_org=st.session_state["qualification_org"],
        issue_date=st.session_state["qualification_issue_date"],
        expiration_date=st.session_state["qualification_expiration_date"],
    )
    st.session_state.qualifications += qualification


def general():
    st.markdown("### General")
    info1, info2, info3, info4, info5 = st.columns(5)
    info1.text_input("Name", key="name")
    info2.text_input("Job Title", key="job_title")
    info3.text_input("Email", key="email")
    info4.text_input("Mobile no.", key="mobile_number")
    info5.text_input("LinkedIn", key="linkedin_url")

    st.text_area("Summary", key="summary")
    st.text_input(
        label="Skills (comma separated list)", on_change=update_skills, key="skill"
    )


def experiences():
    with st.container():
        st.markdown("### Experience")
        e1, e2, e3, e4 = st.columns(4)
        experience_job_title = e1.text_input("Job Title", key="experience_job_title")
        experience_company = e2.text_input("Company", key="experience_company")
        e3.date_input("Start Date", key="experience_start_date")
        current_job = st.checkbox("This is my current job.")
        e4.date_input("End Date", key="experience_end_date", disabled=current_job)
        experience_summary = st.text_area(
            "Summary (markdown supported)", key="experience_summary"
        )
        st.button(
            "Add experience",
            on_click=add_qualification,
            disabled=(
                not experience_job_title
                or not experience_company
                or not experience_summary
            ),
        )


def qualifications():
    with st.container():
        st.markdown("### Qualifications")
        q1, q2, q3, q4 = st.columns(4)
        qualification_name = q1.text_input(
            "Qualification Name", key="qualification_name"
        )
        qualification_org = q2.text_input(
            "Issuing Organisation", key="qualification_org"
        )
        qualification_issue_date = q3.date_input(
            "Issue Date", key="qualification_issue_date"
        )
        not_expires = st.checkbox("This qualification does not expire.")
        q4.date_input(
            "Expiration Date", key="qualification_expiration_date", disabled=not_expires
        )

        st.button(
            "Add qualification",
            on_click=add_qualification,
            disabled=(
                not qualification_name
                or not qualification_org
                or not qualification_issue_date
            ),
        )


def main():
    st.set_page_config(page_title="CV Generator", layout="wide")
    init_session_state()
    st.sidebar.json(st.session_state)

    st.title("📄 CV Generator")

    general()
    experiences()
    qualifications()


if __name__ == "__main__":
    main()
