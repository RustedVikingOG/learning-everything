# .NET Lesson 03: Input Validation & Error Handling

**Date Completed:** February 2, 2026  
**Estimated Time:** ~1.5 hours  
**Report:** [View Report](../../../reports/dotnet/20260202-report.md)  
**Milestone:** 1 - REST API Foundation *(final lesson for M1)*

---

## Objectives ✅

- [x] Add validation to POST endpoints (required fields, data constraints)
- [x] Return appropriate error responses (400 Bad Request)
- [x] Implement a PUT endpoint to complete CRUD operations
- [x] Understand `Results.Created()` with location headers

---

## Key Concepts Covered

1. **Input Validation** - Checking data before processing with `string.IsNullOrWhiteSpace()`
2. **HTTP Status Code Categories** - 4xx (client error) vs 5xx (server error)
3. **Structured Error Responses** - Using records for consistent error formats
4. **PUT Endpoints** - Completing CRUD with update operations
5. **Record Bodies** - Adding computed properties to records

---

## What Was Built

### Validation on POST and PUT
```csharp
if (string.IsNullOrWhiteSpace(itemName.Name))
{
    return Results.BadRequest(new ErrorResponse("ValidationError", "Name", "Item name cannot be empty."));
}
```

### PUT Endpoint for Updates
```csharp
app.MapPut("/items/{id}", (int id, ItemName itemName) =>
{
    if (string.IsNullOrWhiteSpace(itemName.Name))
    {
        return Results.BadRequest(new ErrorResponse("ValidationError", "Name", "Item name cannot be empty."));
    }
    
    var firstItem = items.FirstOrDefault(item => item.Id == id);
    if (firstItem is not null)
    {
        items.Remove(firstItem);
        var updatedItem = new Item(id, itemName.Name);
        items.Add(updatedItem);
        return Results.Ok(updatedItem);
    }
    return Results.NotFound();
});
```

### Structured Error Response
```csharp
record ErrorResponse(string Error, string Field, string Message);
```

### Computed Property on Record
```csharp
record Item(int Id, string Name)
{
    public string DisplayName => Name[0].ToString().ToUpper() + Name[1..];
};
```

---

## Connections Made

- **Status Code Categories:** Connected 4xx = client fault, 5xx = server fault
- **Validation Placement:** Understood trade-offs of validating in records (throws exception) vs handlers (clean HTTP response)
- **IsNullOrWhiteSpace vs IsNullOrEmpty:** Recognized that `" "` passes IsNullOrEmpty but fails IsNullOrWhiteSpace
- **Immutable Records:** Understood why "remove and re-add" pattern is needed for updates
- **curl -v flag:** Learned to debug empty responses by viewing HTTP status codes

---

## Areas Identified for Future Learning

- Data Annotations (`[Required]`, `[MinLength]`) for declarative validation
- Dependency injection and builder pattern
- Database persistence (replacing in-memory List)
- Edge case handling in computed properties

---

## Milestone 1 Status: COMPLETE ✅

| Skill | Status |
|-------|--------|
| Project scaffolding | ✅ |
| Minimal API routing | ✅ |
| Route parameters | ✅ |
| HTTP methods (GET/POST/DELETE) | ✅ |
| HTTP methods (PUT) | ✅ |
| Request/response JSON | ✅ |
| Input validation | ✅ |
| Error handling | ✅ |

**Next:** Capstone Sprint - Build chat rooms and messages API!
