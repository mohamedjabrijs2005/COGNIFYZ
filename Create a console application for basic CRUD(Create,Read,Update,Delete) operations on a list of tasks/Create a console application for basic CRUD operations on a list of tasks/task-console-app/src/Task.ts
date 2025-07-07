class Task {
    id: number;
    title: string;
    description: string;
    completed: boolean;

    constructor(title: string, description: string) {
        this.id = Date.now(); // Using timestamp as a unique ID
        this.title = title;
        this.description = description;
        this.completed = false;
    }

    update(title: string, description: string) {
        this.title = title;
        this.description = description;
    }

    markCompleted() {
        this.completed = true;
    }
}

export default Task;