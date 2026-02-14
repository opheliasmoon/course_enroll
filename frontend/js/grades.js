async function addGrade() {

    const data = {
        student_id: parseInt(document.getElementById("studentID").value),
        course_id: parseInt(document.getElementById("courseID").value),
        grade_value: document.getElementById("gradeValue").value
    };

    await fetch(`${API_URL}/grades`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    loadGrades();
}

async function loadGrades() {

    const response = await fetch(`${API_URL}/grades`);
    const grades = await response.json();

    const list = document.getElementById("gradeList");
    list.innerHTML = "";

    grades.forEach(g => {
        const li = document.createElement("li");
        li.textContent = `Student ${g.student_id} Grade: ${g.grade_value}`;
        list.appendChild(li);
    });
}

loadGrades();
