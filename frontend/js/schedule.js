async function addSchedule() {

    const data = {
        course_id: parseInt(document.getElementById("courseID").value),
        room_number: document.getElementById("room").value,
        day_of_week: document.getElementById("day").value
    };

    await fetch(`${API_URL}/schedules`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    loadSchedules();
}

async function loadSchedules() {

    const response = await fetch(`${API_URL}/schedules`);
    const schedules = await response.json();

    const list = document.getElementById("scheduleList");
    list.innerHTML = "";

    schedules.forEach(s => {
        const li = document.createElement("li");
        li.textContent = `Course ${s.course_id} - ${s.day_of_week} Room ${s.room_number}`;
        list.appendChild(li);
    });
}

loadSchedules();
