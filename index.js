const inputs = document.querySelectorAll("input");
const gallery = document.querySelector(".gallery");

function draw_task(task_name, task_desc, task_end_date, line_through) {
    let task = document.createElement("div");
    task.classList = 'task';
    task.innerHTML = `<table>
            <tr>
                <td>Name:</td>
                <td>${task_name}</td>
            </tr>
            <tr>
                <td>Description:</td>
                <td>${task_desc}</td>
            </tr>
            <tr>
                <td>End date:</td>
                <td>${task_end_date}</td>
            </tr>
        </table>`;
    gallery.appendChild(task);
    if (line_through) {
        task.style.textDecoration = 'line-through';
    }
    task.addEventListener('click', () => {
        console.log(line_through);
        if (line_through) {
            task.style.display = 'none';
            dell_task(task_name);
        }
        else {
            edit_task(task_name)
            task.style.textDecoration = 'line-through';
            line_through = true;
        }
    })
}

async function dell_task(dell_name) {
    let url = `http://127.0.0.1:8000/dell_task/?name=${dell_name}`;

    let response = await fetch(url);

    if (response.ok) {
        let json = await response.json();
        console.log(json);
    }
    else {
        alert("Ошибка HTTP: " + response.status);
    }
}

async function edit_task(edit_name) {
    let url = `http://127.0.0.1:8000/edit_task/?name=${edit_name}`;

    let response = await fetch(url);

    if (response.ok) {
        let json = await response.json();
        console.log(json);
    }
    else {
        alert("Ошибка HTTP:" + response.status);
    }
}

async function create_task() {
    let name = inputs[0].value;
    let ds = inputs[1].value;
    let time = inputs[2].value;
    let lt = false;
    let url = `http://127.0.0.1:8000/create_task/?name=${name}&description=${ds}&end_date=${time}&line_through=false`;
    
    let response = await fetch(url);

    if (response.ok) {
        let json = await response.json();
        console.log(json);
        draw_task(name, ds, time, lt);
    } 
    else {
        alert("Ошибка HTTP: " + response.status);
    }
}

async function get_all_tasks() {
    let url = `http://127.0.0.1:8000/get_all_tasks/`;

    let response = await fetch(url);

    if (response.ok) {
        let json = await response.json();
        console.log(json);
        for (let i = 0; i < json.length; i++) {
            draw_task(
                json[i]['name'],
                json[i]['description'],
                json[i]['end_date'],
                json[i]['line_through'])
        }
    }
    else {
        alert("Ошибка HTTP: " + response.status);
    }
}

inputs[3].addEventListener('click', create_task)

get_all_tasks();

