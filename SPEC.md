# SPEC: To-Do App

This file describes how the app should behave. Fix bugs so the app matches it.

## Behavior

1. **Add:** the user enters a title and adds a task. It appears in the list, not completed.
2. **Complete:** the user marks a task as completed. Only that task changes.
3. **Delete:** the user deletes a task. Only the task with the given ID is removed. All other tasks stay unchanged.
4. **Empty titles:** a title that is empty or only whitespace is rejected. No task is created and the list is unchanged.

## Rules

- Each task has a unique ID.
- Operations on one task never affect other tasks.
- Fix the app code. Do not change tests or this file.
