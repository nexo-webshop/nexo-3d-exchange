; N3X Windows installer definition
; Build with Inno Setup 6 after producing dist\n3x.exe

#define AppName "Nexo 3D Exchange"
#define AppVersion "0.1.0"
#define AppPublisher "Nexo Studios"
#define AppExeName "n3x.exe"

[Setup]
AppId={{B8E6D2D1-9D3C-4D31-A2A0-0A3B6E7D0C11}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher={#AppPublisher}
DefaultDirName={autopf}\Nexo Studios\Nexo 3D Exchange
DefaultGroupName=Nexo 3D Exchange
OutputDir=..\dist-installer
OutputBaseFilename=Nexo3DExchange-Setup-{#AppVersion}
Compression=lzma2
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64compatible
PrivilegesRequired=admin
UninstallDisplayIcon={app}\{#AppExeName}
WizardStyle=modern

[Files]
Source: "..\dist\{#AppExeName}"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Nexo 3D Exchange"; Filename: "{app}\{#AppExeName}"
Name: "{autodesktop}\Nexo 3D Exchange"; Filename: "{app}\{#AppExeName}"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional icons:"
