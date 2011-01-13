; Script initially generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "wxMol"
#define MyAppVersion "0.85"
#define MyAppVerName "wxMol 0.85"
#define MyAppPublisher "Hubert Hanghofer"
#define MyAppURL "http://hubert.hanghofer.net"
#define MyAppExeName "wxMol.exe"
;; !!!ADJUST THIS ONE!!!
;#define MySourceDir "C:\Dokumente und Einstellungen\hubert\Eigene Dateien\PYTHON"
#define MySourceDir "C:\Eigene Dateien\PYTHON"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{E82D9FA9-6D56-49FA-9803-FD77102E726D}
AppName={#MyAppName}
AppVerName={#MyAppVerName}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
;; !!!ADJUST PATH TO SHARED RESOURCES!!!
LicenseFile={#MySourceDir}\shared\licenses\gpl-3_0.txt
OutputBaseFilename={#MyAppName}-{#MyAppVersion}-Setup
Compression=lzma
SolidCompression=yes
;PrivilegesRequired=none

[Languages]
Name: english; MessagesFile: compiler:Default.isl
Name: german; MessagesFile: compiler:Languages\German.isl

[Tasks]
Name: desktopicon; Description: {cm:CreateDesktopIcon}; GroupDescription: {cm:AdditionalIcons}; Flags: unchecked
Name: quicklaunchicon; Description: {cm:CreateQuickLaunchIcon}; GroupDescription: {cm:AdditionalIcons}; Flags: unchecked

[Files]
Source: {#MySourceDir}\mol\dist.w32\wxMol.exe; DestDir: {app}; Flags: ignoreversion
Source: {#MySourceDir}\mol\dist.w32\molcalc.exe; DestDir: {app}; Flags: ignoreversion
Source: {#MySourceDir}\mol\dist.w32\gdiplus.dll; DestDir: {app}; Flags: ignoreversion
Source: {#MySourceDir}\mol\dist.w32\README.TXT; DestDir: {app}; Flags: isreadme
Source: {#MySourceDir}\mol\dist.w32\CHANGELOG.TXT; DestDir: {app}; Flags: ignoreversion
Source: {#MySourceDir}\mol\dist.w32\library.zip; DestDir: {app}; Flags: ignoreversion
Source: {#MySourceDir}\mol\dist.w32\w9xpopen.exe; DestDir: {app}; Flags: ignoreversion
Source: {#MySourceDir}\mol\dist.w32\icons\tick.xpm; DestDir: {app}\icons; Flags: ignoreversion
Source: {#MySourceDir}\mol\dist.w32\icons\copy.xpm; DestDir: {app}\icons; Flags: ignoreversion
Source: {#MySourceDir}\mol\dist.w32\icons\benzol.ico; DestDir: {app}\icons; Flags: ignoreversion

;; Either install msvc runtime via vcredist_x86.exe...
;; (http://www.microsoft.com/downloads/details.aspx?FamilyID=9b2da534-3e03-4391-8a4d-074b9f2bc1bf&displaylang=en)
Source: {#MySourceDir}\shared\Microsoft.VC90.CRT\vcredist_x86.exe; DestDir: {tmp}; Permissions: everyone-full; Flags: ignoreversion overwritereadonly

;; ...or as a private assembly in the {app} Directory.
;; !!!REMEMBER TO ADJUST PATH FOR PULLING IN RESOURCES SHARED BY YOUR PROJECTS!!!
;Source: {#MySourceDir}\shared\Microsoft.VC90.CRT\Microsoft.VC90.CRT.manifest; DestDir: {app}; Flags: ignoreversion
;Source: {#MySourceDir}\shared\Microsoft.VC90.CRT\msvcp90.dll; DestDir: {app}; Flags: ignoreversion
;Source: {#MySourceDir}\shared\Microsoft.VC90.CRT\msvcr90.dll; DestDir: {app}; Flags: ignoreversion
; NOTE: "Flags: ignoreversion" is safe to use for private assembly. Don't use it on any shared system files

[Icons]
; ADD WorkingDir so that application icons can be found!!!
Name: {group}\{#MyAppName}; Filename: {app}\{#MyAppExeName}; WorkingDir: {app}
Name: {group}\{cm:ProgramOnTheWeb,{#MyAppName}}; Filename: {#MyAppURL}
Name: {group}\{cm:UninstallProgram,{#MyAppName}}; Filename: {uninstallexe}
Name: {commondesktop}\{#MyAppName}; Filename: {app}\{#MyAppExeName}; WorkingDir: {app}; Tasks: desktopicon
Name: {userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}; Filename: {app}\{#MyAppExeName}; WorkingDir: {app}; Tasks: quicklaunchicon

[Run]
; Install msvc runtime - for parameter details see this blog entry:
; http://blogs.msdn.com/astebner/archive/2009/03/26/9513328.aspx
Filename: {tmp}\vcredist_x86.exe; Parameters: /qb!; WorkingDir: {tmp}; StatusMsg: Checking for and installing Microsoft Visual C++ Redistributable Package...; Flags: waituntilterminated
Filename: {app}\{#MyAppExeName}; Description: {cm:LaunchProgram,{#MyAppName}}; Flags: nowait postinstall skipifsilent




