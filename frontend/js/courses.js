async function addCourse() {

    const data = {
        course_name: document.getElementById("courseName").value,
        credits: parseInt(document.getElementById("credits").value),
        department: document.getElementById("department").value
    };

    await fetch(`${API_URL}/courses`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    loadCourses();
}

async function loadCourses() {

    const response = await fetch(`${API_URL}/courses`);
    const courses = await response.json();

    const list = document.getElementById("courseList");
    list.innerHTML = "";

    courses.forEach(c => {
        const li = document.createElement("li");
        li.textContent = `${c.course_name} (${c.department})`;
        list.appendChild(li);
    });
}

loadCourses();
