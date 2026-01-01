---
description: "Task list for Interactive Todo Console App implementation"
---

# Tasks: Interactive Todo Console App

**Input**: Design documents from `/specs/001-interactive-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Constitution Compliance**: All tasks MUST comply with Phase I Console Todo Application Constitution:
- Tech Stack: Python 3.13+ with UV package manager
- Storage: In-memory only (no external databases or file storage)
- Architecture: Modular design with separate Data Model, Logic, and UI
- Code Quality: PEP 8 compliant, fully type-hinted, with docstrings
- User Experience: Interactive CLI with step-by-step prompts
- Development: Spec-Driven Development with Task IDs
- Deployment: No deployment configurations for Phase I

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 [P] Create src directory with empty __init__.py file
- [X] T003 [P] Create pyproject.toml with Python 3.13+ requirement

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T004 Implement Task data class in src/models.py with id, title, description, completed fields
- [X] T005 [P] Implement TaskManager class in src/manager.py with in-memory storage (list/dict)
- [X] T006 [P] Create basic InteractiveCLI class in src/ui.py with main loop structure
- [X] T007 Create entry point in src/main.py that initializes components and starts loop
- [X] T008 Implement README.md with usage instructions

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Interactive Task Addition (Priority: P1) 🎯 MVP

**Goal**: Enable users to add tasks through interactive prompts

**Independent Test**: Can be fully tested by entering "add" command, providing a title and description, and verifying that a new task is created and displayed in the task list.

### Implementation for User Story 1

- [X] T009 [US1] Implement add_task method in src/manager.py that creates new tasks with auto-generated IDs
- [X] T010 [US1] Implement prompt_for_add method in src/ui.py that asks for title and description using input()
- [X] T011 [US1] Implement add command handler in InteractiveCLI that connects UI prompts to manager
- [X] T012 [US1] Add validation to ensure title is non-empty in both UI and manager layers
- [X] T013 [US1] Update main loop in src/ui.py to recognize "add" command and route to add handler

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 4 - View Tasks (Priority: P1)

**Goal**: Display all tasks with [x] for completed and [ ] for incomplete

**Independent Test**: Can be fully tested by creating multiple tasks, marking some as complete, and verifying the display format shows [x] for completed and [ ] for incomplete tasks.

### Implementation for User Story 4

- [X] T014 [US4] Implement get_all_tasks method in src/manager.py that returns all tasks
- [X] T015 [US4] Implement display_tasks method in src/ui.py that formats and prints tasks with [x]/[ ] indicators
- [X] T016 [US4] Implement view command handler in InteractiveCLI that connects manager to display
- [X] T017 [US4] Update main loop in src/ui.py to recognize "view" or "list" command and route to view handler
- [X] T018 [US4] Handle empty task list case with appropriate message

**Checkpoint**: At this point, User Stories 1 AND 4 should both work independently

---

## Phase 5: User Story 2 - Interactive Task Update (Priority: P2)

**Goal**: Allow users to update existing tasks by ID

**Independent Test**: Can be fully tested by creating a task, using "update" command with a valid ID, and verifying that the task details are updated.

### Implementation for User Story 2

- [X] T019 [US2] Implement update_task method in src/manager.py that updates title/description by ID
- [X] T020 [US2] Implement prompt_for_id method in src/ui.py that asks for task ID using input()
- [X] T021 [US2] Implement update command handler in InteractiveCLI that connects UI prompts to manager
- [X] T022 [US2] Add error handling for invalid IDs in update process
- [X] T023 [US2] Update main loop in src/ui.py to recognize "update" command and route to update handler

**Checkpoint**: At this point, User Stories 1, 4, AND 2 should all work independently

---

## Phase 6: User Story 3 - Interactive Task Actions (Priority: P3)

**Goal**: Allow users to delete or complete tasks by ID

**Independent Test**: Can be fully tested by using "delete" or "complete" commands with valid and invalid IDs, verifying appropriate responses.

### Implementation for User Story 3

- [X] T024 [US3] Implement delete_task method in src/manager.py that removes tasks by ID
- [X] T025 [US3] Implement complete_task method in src/manager.py that marks tasks as completed
- [X] T026 [US3] Implement delete command handler in InteractiveCLI that connects UI prompts to manager
- [X] T027 [US3] Implement complete command handler in InteractiveCLI that connects UI prompts to manager
- [X] T028 [US3] Update main loop in src/ui.py to recognize "delete" and "complete" commands
- [X] T029 [US3] Add comprehensive error handling for invalid IDs with "Invalid ID, try again" message

**Checkpoint**: All user stories should now be independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T030 [P] Add docstrings to all functions and classes in all modules
- [X] T031 [P] Ensure all code is PEP 8 compliant and fully type-hinted
- [X] T032 Add error handling to prevent crashes when invalid IDs are entered
- [X] T033 Add continuous loop functionality that continues until user exits
- [X] T034 Implement proper menu display showing available commands
- [X] T035 Run quickstart.md validation to ensure all functionality works as expected

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P1)**: Can start after Foundational (Phase 2) - May depend on US1 for data to display
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US4 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US4 but should be independently testable

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 4 → Test independently → Deploy/Demo
4. Add User Story 2 → Test independently → Deploy/Demo
5. Add User Story 3 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 4
   - Developer C: User Story 2
   - Developer D: User Story 3
3. Stories complete and integrate independently