async function assignInstructor() {

    const data = {
        instructor_id: parseInt(document.getElementById("instructorID").value),
        course_id: parseInt(document.getElementById("courseID").value)
    };

    await fetch(`${API_URL}/assignments`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    loadAssignments();
}

async function loadAssignments() {

    const response = await fetch(`${API_URL}/assignments`);
    const assignments = await response.json();

    const list = document.getElementById("assignList");
    list.innerHTML = "";

    assignments.forEach(a => {
        const li = document.createElement("li");
        li.textContent = `Instructor ${a.instructor_id} teaches Course ${a.course_id}`;
        list.appendChild(li);
    });
}

loadAssignments();
