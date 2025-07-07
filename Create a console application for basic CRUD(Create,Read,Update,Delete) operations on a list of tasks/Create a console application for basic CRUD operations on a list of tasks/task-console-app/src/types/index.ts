export interface TaskInput {
    title: string;
    description: string;
}

export interface TaskOutput {
    id: number;
    title: string;
    description: string;
    completed: boolean;
}