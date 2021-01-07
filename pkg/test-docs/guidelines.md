# Expected Outcomes

**Innacurate Title Metadata**
* filterbubble-acm-xrds
* cscw2014_fiesler

**Missing Title Metadata**
* Baldridge_Colt_Resume.pdf
* Unix-Linux Command Reference.pdf

**Accurate Title Metadata**
* Eternal October and the End of Cyberspace.pdf

**Accurate But Illegal Title Metadata**
* experiment.pdf
* lobby_guide.pdf

# Expected Name Changes

# Required Methods
* Acurate title - rename()
* Missing - Error: Missing. shutil.move()
* Innacurate - Error: Innacurate
* Illegal - Entry.__format()
*   - Exception

## Possible Code Revisions
Instead of multiple output folders within the working directory, store them
within a main parent folder.

**Proposed Hierarchy**
working-directory
    pdf-renamer
        backup
        missed-files
        innacurate-titles
        missing-data
