Sure! I’ll explain **step-by-step** for the **Jenkins Task Sheet (Assessment-2)** exactly in the order given in your PDF. 

---

# ✅ TASK 1: Jenkins Familiarization

### Step 1: Open Jenkins

* Open browser
* Type:
  `http://localhost:8080`
  (or your Jenkins server IP)

### Step 2: Identify Jenkins UI parts

On the Dashboard page locate:

* **Dashboard** (Home page)
* **Manage Jenkins** (left side menu)
* **New Item** (to create job)
* **Build History** (left side)

### Step 3: Check Jenkins Version

* Click **Manage Jenkins**
* Scroll down and click **About Jenkins**
* Note the version (Example: Jenkins 2.440.1)

✅ Output: Screenshot / version note

---

# ✅ TASK 2: Create First Freestyle Job

### Step 1: Create Job

* Click **New Item**
* Enter name: `Hello-Jenkins`
* Select: **Freestyle project**
* Click **OK**

### Step 2: Add Description

* In Description box type:
  `My first Jenkins job`

### Step 3: Add Build Step

* Scroll to **Build**
* Click **Add build step**
* Choose:

  * **Execute shell** (Linux)
  * **Execute Windows batch command** (Windows)

Add command:

```bash
echo "Hello Jenkins"
```

### Step 4: Save & Build

* Click **Save**
* Click **Build Now**

### Step 5: View Output

* Click build number (#1)
* Click **Console Output**

✅ Output: "Hello Jenkins" displayed

---

# ✅ TASK 3: Jenkins Workspace & Commands

### Step 1: Open Workspace

* Open job `Hello-Jenkins`
* Click **Workspace**

### Step 2: Create a text file using build step

Go to job configuration:

* Click **Configure**
* In Build Step add:

```bash
echo "This is my Jenkins workspace file" > sample.txt
cat sample.txt
```

### Step 3: Save and Build

* Save
* Build Now
* Check Console Output

### Step 4: Verify in Workspace

* Open Workspace again
* You will see `sample.txt`

✅ Output: file created and displayed

---

# ✅ TASK 4: Git Integration

### Step 1: Create GitHub Repo

* Open GitHub
* Create new repository (example: `jenkins-demo`)
* Add sample code file like `index.html` or `Hello.java`

### Step 2: Install Git Plugin in Jenkins

* Manage Jenkins → Plugins
* Search **Git plugin**
* Install

### Step 3: Configure Git in Jenkins Job

* Go to job → Configure
* Under **Source Code Management**
* Select **Git**
* Paste GitHub URL:
  `https://github.com/username/jenkins-demo.git`

### Step 4: Save and Build

* Save
* Build Now

### Step 5: Verify Code in Workspace

* Open Workspace
* You should see repository files

✅ Output: Code visible in workspace

---

# ✅ TASK 5: Poll SCM Trigger

### Step 1: Enable Poll SCM

* Configure job
* Go to **Build Triggers**
* Tick **Poll SCM**

### Step 2: Set Schedule

Enter:

```
* * * * *
```

### Step 3: Commit Changes in GitHub

* Edit any file
* Commit changes

### Step 4: Observe Jenkins Build

* Jenkins will automatically build within 1 minute

✅ Output: Build triggered automatically

---

# ✅ TASK 6: Parameterized Build

### Step 1: Enable Parameterized Build

* Configure job
* Tick **This project is parameterized**

### Step 2: Add String Parameter

* Click **Add Parameter**
* Choose **String Parameter**
* Name: `USERNAME`
* Default value: `Student`

### Step 3: Print Parameter in Build Step

In Execute Shell:

```bash
echo "Hello $USERNAME"
```

### Step 4: Save and Build

* Click **Build with Parameters**
* Enter name and build

✅ Output: Username printed

---

# ✅ TASK 7: Java Build Using Jenkins

### Step 1: Create Hello.java in GitHub repo

Example:

```java
class Hello {
    public static void main(String args[]) {
        System.out.println("Hello from Java using Jenkins");
    }
}
```

### Step 2: Configure Jenkins Build Step

In Execute Shell:

```bash
javac Hello.java
java Hello
```

### Step 3: Build Now

Check Console Output

✅ Output: Java program output

---

# ✅ TASK 8: Archive Artifacts

### Step 1: Generate .class file

Build should generate:
`Hello.class`

### Step 2: Add Post-build Action

* Configure job
* Scroll to **Post-build Actions**
* Click **Add post-build action**
* Select **Archive the artifacts**

### Step 3: Enter artifact name

Example:

```
*.class
```

### Step 4: Save and Build

After build:

* On job page you will see **Last Successful Artifacts**
* Download file

✅ Output: Artifact downloadable

---

# ✅ TASK 9: Users & Roles

### Step 1: Enable Security

* Manage Jenkins → Security
* Configure Global Security
* Enable security

### Step 2: Create Two Users

* Manage Jenkins → Users → Create User
  Create:
* user1 (read-only)
* user2 (build access)

### Step 3: Install Role Strategy Plugin

* Manage Jenkins → Plugins
* Install: **Role-based Authorization Strategy**

### Step 4: Assign Permissions

* Manage Jenkins → Security → Authorization
* Choose Role-based Strategy
  Assign:
* user1 → Read only
* user2 → Build permission

### Step 5: Verify

Login with both users and check access

✅ Output: Permission differences verified

---

# ✅ TASK 10: Simple Jenkins Pipeline

### Step 1: Create Pipeline Job

* New Item
* Name: `Simple-Pipeline`
* Select **Pipeline**
* Click OK

### Step 2: Write Pipeline Script

Paste:

```groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out code"
            }
        }

        stage('Build') {
            steps {
                echo "Building project"
            }
        }

        stage('Test') {
            steps {
                echo "Running tests"
            }
        }
    }
}
```

### Step 3: Save and Build

* Save
* Build Now

✅ Output: Stage View displayed

---

# ✅ TASK 11: Jenkinsfile from Git

### Step 1: Create Jenkinsfile in GitHub Repo

Add file: `Jenkinsfile`

Example:

```groovy
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/username/jenkins-demo.git'
            }
        }
        stage('Build') {
            steps {
                echo "Build Stage"
            }
        }
        stage('Test') {
            steps {
                echo "Test Stage"
            }
        }
    }
}
```

### Step 2: Configure Jenkins Pipeline from SCM

* Create Pipeline job
* In Pipeline section select:
  **Pipeline script from SCM**
* SCM: Git
* Repo URL: your repo
* Script path: `Jenkinsfile`

### Step 3: Build Now

✅ Output: Pipeline executed from Git

---

# ✅ TASK 12: Post-Build Actions (Success/Failure)

### Step 1: Add Post section in Jenkinsfile

Example:

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Building..."
            }
        }
    }

    post {
        success {
            echo "Build Successful!"
        }
        failure {
            echo "Build Failed!"
        }
    }
}
```

### Step 2: Run Pipeline

✅ Output: correct message based on result

---

# ✅ TASK 13: Trigger Job from Another Job

### Step 1: Create Job-A

* New Item → Freestyle → Name: Job-A
* Add build step: echo "Job A running"

### Step 2: Create Job-B

* New Item → Freestyle → Name: Job-B
* Add build step: echo "Job B running"

### Step 3: Configure Job-A to Trigger Job-B

* Go to Job-A → Configure
* Post-build Actions
* Select **Build other projects**
* Enter: `Job-B`

### Step 4: Build Job-A

Job-B will run automatically

✅ Output: Job-B triggered after Job-A

---

# ✅ TASK 14: Workspace Cleanup

### Step 1: Install Plugin

* Manage Jenkins → Plugins
* Install: **Workspace Cleanup Plugin**

### Step 2: Configure Cleanup

* Configure job
* Tick: **Delete workspace before build starts**
  (or add build environment option)

### Step 3: Build Job

Workspace will be cleared first

✅ Output: workspace cleaned

---

# ✅ TASK 15: Mini CI Project

### Step 1: Git commit triggers Jenkins build

* Use Poll SCM or Webhook

### Step 2: Checkout code

* Jenkins pulls repo

### Step 3: Compile code

Example build step:

```bash
javac Hello.java
```

### Step 4: Archive artifacts

Add:

```
*.class
```

### Step 5: Fail build on error

If compilation fails Jenkins automatically marks build FAILED.

✅ Output: Automated CI pipeline working

---

# ✅ CI Tool Study Part (Companies using Jenkins)

Companies known to use Jenkins include:

* Netflix
* LinkedIn
* Facebook (Meta)
* IBM
* Oracle
* Cisco
* Red Hat
* eBay

---

If you want, I can also prepare this as a **neat lab record write-up format** (Aim, Steps, Output) for submission.
