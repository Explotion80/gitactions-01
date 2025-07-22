var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.MapGet("/secret", (string? password) =>
{
    if (password == "secret123")
    {
        return "Nice you are our agent";
    }
    else
    {
        return "You are not our agent";
    }
});

app.Run();
