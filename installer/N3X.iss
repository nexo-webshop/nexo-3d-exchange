; N3X Windows installer
#define AppName "Nexo 3D Exchange"
#define AppVersion "0.1.0"
#define Publisher "Nexo Studios"

[Setup]
AppId={{A6A4A2D0-6E1B-4B51-9C4A-7B4E2B7C9F01}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher={#Publisher}
DefaultDirName={autopf}\Nexo 3D Exchange
DefaultGroupName={#AppName}
OutputDir=dist
OutputBaseFilename=Nexo-3D-Exchange-Setup-{#AppVersion}
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64compatible
PrivilegesRequired=admin
WizardStyle=modern

[Files]
Source: "..\dist\n3x.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Nexo 3D Exchange"; Filename: "{app}\n3x.exe"
Name: "{autodesktop}\Nexo 3D Exchange"; Filename: "{app}\n3x.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional icons:"

[Run]
Filename: "{app}\n3x.exe"; Description: "Run Nexo 3D Exchange"; Flags: nowait postinstall skipifsilent
