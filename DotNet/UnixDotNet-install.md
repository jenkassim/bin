# DotNet on Linux

## Installation:
```
$ sudo dnf update
$ sudo dnf install libunwind libicu compat-openssl10
$ sudo dnf install dotnet-sdk-2.1.4
```

## Create new App
```
    $ dotnet new console -o myApp
    $ cd myApp
```

## Run the App
```
    $ dotnet run
```

## Links
- Quick start Collections
https://docs.microsoft.com/en-us/dotnet/csharp/quick-starts/arrays-and-collections


# Welcome to .NET Core!
Learn more about .NET Core @ https://aka.ms/dotnet-docs. Use dotnet --help to see available commands or go to https://aka.ms/dotnet-cli-docs.

## Telemetry
The .NET Core tools collect usage data in order to improve your experience. The data is anonymous and does not include command-line arguments. The data is collected by Microsoft and shared with the community.
You can opt out of telemetry by setting a DOTNET_CLI_TELEMETRY_OPTOUT environment variable to 1 using your favorite shell.
You can read more about .NET Core tools telemetry @ https://aka.ms/dotnet-cli-telemetry.
Getting ready...
The template "Console Application" was created successfully.

Processing post-creation actions...
Running 'dotnet restore' on myApp/myApp.csproj...
  Restoring packages for /home/jenna_mk/dev/code/dotnet/myApp/myApp.csproj...
  Generating MSBuild file /home/jenna_mk/dev/code/dotnet/myApp/obj/myApp.csproj.nuget.g.props.
  Generating MSBuild file /home/jenna_mk/dev/code/dotnet/myApp/obj/myApp.csproj.nuget.g.targets.
  Restore completed in 170.53 ms for /home/jenna_mk/dev/code/dotnet/myApp/myApp.csproj.

Restore succeeded.

