# 🗄️ Lesson 04: Entity Framework Core Basics

**Type:** Lesson (Theory + Practice)
**Estimated Time:** 1.5 hours
**Milestone:** 2 - Data Persistence

---

## 🎯 Objectives

1.  **Understand ORMs:** What is Entity Framework Core and why do we use it?
2.  **Install EF Core:** Add packages to the project.
3.  **Create a DbContext:** The bridge between code and data.
4.  **Entities vs DTOs:** Refactoring our `record` models into proper Entities.
5.  **In-Memory Database:** Using EF Core's in-memory provider (for testing/learning before SQL).

---

## 📚 Theory: The Persistence Layer

Currently, `var rooms = new List<Room>();` dies when the app stops.
To save data, we need a database. But writing raw SQL (`SELECT * FROM Rooms`) is tedious and error-prone.

**Enter EF Core (ORM):**
- **ORM:** Object-Relational Mapper.
- Maps C# Objects (`Room`) <--> Database Rows (Table `Rooms`).
- We write C#, EF writes the SQL.

### Key Components
1.  **Entity:** A class representing a table (e.g., `class Room { Id, Name }`).
2.  **DbContext:** Represents a session with the database. Manages saving/retrieving entities.
3.  **DbSet<T>:** Represents a table inside the DbContext.

---

## 📖 External Resources (Mandatory)

Before proceeding with the exercises, please review the following official documentation to understand the tools you will be using:
- [EF Core InMemory Database Provider](https://learn.microsoft.com/en-us/ef/core/providers/in-memory/)
- [DbContext Lifetime, Configuration, and Initialization](https://learn.microsoft.com/en-us/ef/core/dbcontext-configuration/)

---

## 💡 Analogous Examples

*(Review these examples of how to set up EF Core for a completely different domain (`Library`), then apply the concepts to your `WebChatApi` domain.)*

```csharp
// 1. Entity Definition (Mutable Class)
public class Book 
{
    public string Isbn { get; set; } = Guid.NewGuid().ToString();
    public string Title { get; set; } = string.Empty;
}

// 2. DbContext Definition
public class LibraryDbContext : DbContext
{
    public LibraryDbContext(DbContextOptions<LibraryDbContext> options) : base(options) {}
    public DbSet<Book> Books => Set<Book>();
}

// 3. Registering in Program.cs
builder.Services.AddDbContext<LibraryDbContext>(opt => opt.UseInMemoryDatabase("LibraryDB"));

// 4. Using the DB in an Endpoint (Async)
app.MapGet("/books", async (LibraryDbContext db) => {
    return await db.Books.ToListAsync();
});
app.MapPost("/books", async (Book newBook, LibraryDbContext db) => {
    db.Books.Add(newBook);
    await db.SaveChangesAsync();
    return Results.Created($"/books/{newBook.Isbn}", newBook);
});
```

---

## 🏗️ Exercises

### 1. Project Setup
We will continue working on your **WebChatApi**.
- **Requirement:** Install the `Microsoft.EntityFrameworkCore.InMemory` NuGet package.

### 2. Define Entities
- **Requirement:** Refactor your `Room` and `Message` models from `record` (immutable) to `class` (mutable, which is easier for EF to track). Ensure they have an Id property and default values for properties like `CreatedAt`.

### 3. The AppDbContext
- **Requirement:** Create a new class `AppDbContext` in a `Data/` folder. It must inherit from `DbContext` and contain `DbSet` properties for both `Rooms` and `Messages`.

### 4. Dependency Injection
- **Requirement:** Wire up your `AppDbContext` in `Program.cs` to use the InMemory database provider. Name the database "WebChat".

### 5. Refactor Endpoints
- **Requirement:** Replace the static `List<Room>` and `List<Message>` in your minimal API endpoints with dependency-injected `AppDbContext`.
- **Constraint:** All external database calls (like reading all rooms or saving changes) must be strictly **asynchronous** (e.g., `ToListAsync()`, `SaveChangesAsync()`). No blocking `.ToList()` calls!
- **Constraint:** Handle basic error states (e.g., trying to write a message to a RoomId that doesn't exist).

---

## 🧪 Success Criteria

- [ ] `Microsoft.EntityFrameworkCore.InMemory` package installed.
- [ ] `AppDbContext` created and registered in DI.
- [ ] Endpoints refactored to use asynchronous database calls (`ToListAsync`, `SaveChangesAsync`).
- [ ] Attempting to write a message to a non-existent room returns a 404 (or appropriate error).
- [ ] App behaves exactly as before but uses EF Core syntax.

---

## 🧠 Check for Understanding

- Why do we need a `DbContext`?
- What is difference between `List.Add()` and `db.Rooms.Add()`? (Hint: `SaveChanges`)
- Why must we use asynchronous methods like `ToListAsync()` when working with databases instead of synchronous methods like `ToList()`?
