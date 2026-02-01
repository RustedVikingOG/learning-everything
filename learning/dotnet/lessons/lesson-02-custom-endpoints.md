# .NET Lesson 02: Custom Endpoints & Route Parameters

**Date Started:**  
**Estimated Time:** 2-3 hours  
**Issue:** [#5](https://github.com/RustedVikingOG/learning-everything/issues/5)  
**Milestone:** 1 - REST API Foundation

---

## Objectives

- [ ] Add a custom GET endpoint with a route parameter (`/hello/{name}`)
- [ ] Add a POST endpoint that accepts JSON body data
- [ ] Understand HTTP methods in ASP.NET Core (MapGet, MapPost, MapPut, MapDelete)
- [ ] Return different response types (string, JSON, status codes)

---

## Key Concepts

1. **Route Parameters** - Capturing values from the URL path
2. **Request Body** - Accepting JSON data in POST/PUT requests
3. **HTTP Methods** - When to use GET vs POST vs PUT vs DELETE
4. **Response Types** - `Results.Ok()`, `Results.NotFound()`, `Results.Created()`

---

## Exercises

### Exercise 1: Hello Endpoint
Create `/hello/{name}` that returns `"Hello, {name}!"`.

**Test with:**
```bash
curl http://localhost:5000/hello/World
# Expected: "Hello, World!"
```

### Exercise 2: Echo Endpoint  
Create `POST /echo` that accepts JSON and returns it back.

**Test with:**
```bash
curl -X POST http://localhost:5000/echo \
  -H "Content-Type: application/json" \
  -d '{"message": "test"}'
```

### Exercise 3: Simple CRUD
Add endpoints to manage a list of items in memory:
- `GET /items` - list all
- `GET /items/{id}` - get one
- `POST /items` - add new
- `DELETE /items/{id}` - remove

---

## Before Starting

- [ ] Review `Program.cs` from Lesson 1
- [ ] Have `first-dotnet-webapi` project ready
- [ ] Keep a terminal open for `dotnet run`

---

## Notes

_Space for learnings, discoveries, and "aha" moments during the lesson_

---

## Connections to Prior Knowledge

| .NET Concept | Prior Knowledge |
|--------------|-----------------|
| Route params `{name}` | Vue Router `:id` params |
| `Results.Ok()` | Express `res.json()` |
| `Results.NotFound()` | Express `res.status(404)` |
| In-memory list | Vue component state |

---

## Summary

_To be completed after lesson_
