async function enroll() {

    const data = {
        student_id: parseInt(document.getElementById("studentID").value),
        course_id: parseInt(document.getElementById("courseID").value),
        enrollment_status: "Active"
    };

    await fetch(`${API_URL}/enrollments`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    loadEnrollments();
}

async function loadEnrollments() {

    const response = await fetch(`${API_URL}/enrollments`);
    const enrollments = await response.json();

    const list = document.getElementById("enrollList");
    list.innerHTML = "";

    enrollments.forEach(e => {
        const li = document.createElement("li");
        li.textContent = `Student ${e.student_id} → Course ${e.course_id}`;
        list.appendChild(li);
    });
}

loadEnrollments();
