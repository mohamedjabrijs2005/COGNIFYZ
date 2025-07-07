import * as readline from 'readline';
import { Task } from './Task';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let tasks: Task[] = [];
let nextId = 1;

const mainMenu = () => {
    console.log('\nTask Console App');
    console.log('1. Create Task');
    console.log('2. Read Tasks');
    console.log('3. Update Task');
    console.log('4. Delete Task');
    console.log('5. Exit');
    rl.question('Choose an option: ', handleMenuChoice);
};

const handleMenuChoice = (choice: string) => {
    switch (choice) {
        case '1':
            createTask();
            break;
        case '2':
            readTasks();
            break;
        case '3':
            updateTask();
            break;
        case '4':
            deleteTask();
            break;
        case '5':
            rl.close();
            break;
        default:
            console.log('Invalid choice. Please try again.');
            mainMenu();
            break;
    }
};

const createTask = () => {
    rl.question('Enter task title: ', (title) => {
        rl.question('Enter task description: ', (description) => {
            const task = new Task(nextId++, title, description);
            tasks.push(task);
            console.log('Task created:', task);
            mainMenu();
        });
    });
};

const readTasks = () => {
    if (tasks.length === 0) {
        console.log('No tasks available.');
    } else {
        tasks.forEach(task => {
            console.log(`ID: ${task.id}, Title: ${task.title}, Completed: ${task.completed}`);
        });
    }
    mainMenu();
};

const updateTask = () => {
    rl.question('Enter task ID to update: ', (idStr) => {
        const id = parseInt(idStr);
        const task = tasks.find(t => t.id === id);
        if (task) {
            rl.question('Enter new title: ', (title) => {
                rl.question('Enter new description: ', (description) => {
                    task.update(title, description);
                    console.log('Task updated:', task);
                    mainMenu();
                });
            });
        } else {
            console.log('Task not found.');
            mainMenu();
        }
    });
};

const deleteTask = () => {
    rl.question('Enter task ID to delete: ', (idStr) => {
        const id = parseInt(idStr);
        tasks = tasks.filter(t => t.id !== id);
        console.log(`Task with ID ${id} deleted.`);
        mainMenu();
    });
};

mainMenu();