// Interface
public interface IDataService
{
    string GetData();
}

// Concrete implementation
public class DataService : IDataService
{
    public string GetData()
    {
        return "Data from DataService";
    }
}

// Example usage in a controller (ASP.NET Core)
public class MyController : Controller
{
    private readonly IDataService _dataService;

    // Constructor injection
    public MyController(IDataService dataService)
    {
        _dataService = dataService;
    }

    public IActionResult Index()
    {
        string data = _dataService.GetData();
        return View(data);
    }
}

// Registering the service (Startup.cs or Program.cs - .NET 6+)
builder.Services.AddScoped<IDataService, DataService>(); // Or AddTransient, AddSingleton

// Benefits of DI:
// - Loose coupling:  Makes code more testable and maintainable.
// - Reusability:  Services can be easily reused across the application.
// - Testability:  Mocking dependencies during unit testing becomes easier.


public static string ReverseStringIterative(string str)
{
    char[] charArray = str.ToCharArray();
    int left = 0;
    int right = str.Length - 1;

    while (left < right)
    {
        char temp = charArray[left];
        charArray[left] = charArray[right];
        charArray[right] = temp;
        left++;
        right--;
    }

    return new string(charArray);
}