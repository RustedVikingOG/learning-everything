# .NET Lesson 01: Web API Basics

**Date Completed:** January 31, 2026  
**Estimated Time:** 4 hours (actual)  
**Report:** [20260131-report.md](../../reports/dotnet/20260131-report.md)  
**Milestone:** 1 - REST API Foundation

---

## Objectives

- [x] Install .NET SDK
- [x] Scaffold a new Web API project (`dotnet new webapi`)
- [x] Run the API and test an endpoint
- [x] Understand records and computed properties
- [x] Understand basic type safety
- [x] Basic LINQ introduction
- [x] Minimal API routing basics

---

## Key Concepts Covered

1. **Project Scaffolding** - Using `dotnet new webapi` to generate a project
2. **Records** - Immutable data structures with computed properties
3. **Type Safety** - `int`, `string?`, `DateOnly`, nullable types
4. **LINQ** - `Enumerable.Range`, `.Select()`, `.ToArray()`
5. **Minimal APIs** - `MapGet` for routing

---

## What Was Built

- `first-dotnet-webapi` project with default weather forecast endpoint
- Successfully tested endpoint via curl

---

## Connections Made

| .NET Concept | Prior Knowledge |
|--------------|-----------------|
| `.csproj` | `package.json` (Node.js) |
| `obj/` folder | `node_modules/` |
| `MapGet` | Express.js routing |
| LINQ `.Select()` | JavaScript `.map()` |
| `Program.cs` | `App.vue` entry point |

---

## Areas Identified for Next Lesson

- Route parameters (`/hello/{name}`)
- POST/PUT/DELETE endpoints
- Request body handling
- HTTP method semantics
