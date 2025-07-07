# Task Console Application

This is a simple console application for managing tasks using basic CRUD operations. The application allows users to create, read, update, and delete tasks.

## Project Structure

```
task-console-app
├── src
│   ├── index.ts          # Entry point of the application
│   ├── Task.ts           # Task class definition
│   └── types
│       └── index.ts      # Type definitions for tasks
├── package.json          # NPM package configuration
├── tsconfig.json         # TypeScript configuration
└── README.md             # Project documentation
```

## Getting Started

### Prerequisites

- Node.js (version 12 or higher)
- npm (Node package manager)

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd task-console-app
   ```
3. Install the dependencies:
   ```
   npm install
   ```

### Running the Application

To run the application, use the following command:
```
npm start
```

### Usage

Once the application is running, you can perform the following operations:

- **Create a Task**: Provide a title and description to create a new task.
- **Read Tasks**: View all existing tasks.
- **Update a Task**: Select a task and update its title and description.
- **Delete a Task**: Remove a task from the list.

### Example

1. Create a new task:
   ```
   Create Task: Title: "Buy groceries", Description: "Milk, Bread, Eggs"
   ```

2. View all tasks:
   ```
   Tasks:
   1. Buy groceries - Not Completed
   ```

3. Update a task:
   ```
   Update Task 1: New Title: "Buy groceries and fruits", New Description: "Milk, Bread, Eggs, Apples"
   ```

4. Delete a task:
   ```
   Delete Task 1
   ```

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.

## License

This project is licensed under the MIT License.


## Author

**Mohamed Jabri J S**