# Windows Build

The official Windows build is performed by GitHub Actions.

## Starting a build

The workflow is deliberately manual.

1. Open the repository on GitHub.
2. Open Actions.
3. Select Build Nexo 3D Exchange.
4. Select Run workflow.
5. Wait for the Windows build to finish.
6. Download the generated artifacts.

## Build outputs

The workflow produces a Windows installer and the standalone executable.

The installer is an Inno Setup EXE. The executable is produced with PyInstaller.

## Build gates

The workflow does not package software when the automated test suite fails.

The build also verifies that the generated executable starts and responds to --help.
