# AWSRekognition
An image label generator using Amazon Rekognition, enabling it to identify objects in photos and automatically assign relevant labels.


# 🖼️ **Image Labels Generator – Powered by Amazon Rekognition**  

## 🔹 **Overview of Project** ☁️  
This project was built as part of **TechWithLucy’s course**, where I learned to use **Amazon Rekognition** to create an **image labeling tool**.  
Once completed, this tool can:  
✅ **Recognize objects in images**  
✅ **Generate labels based on image content**  
✅ **Store and analyze images using AWS services**  

## 🔹 **How I Built It**  
I started by following each of the steps in the course and thought, _“This is pretty cool!”_ So, I decided to test it on a **busy street scene** downloaded from Alamy.com.  
The image contained **people, bikes, cars, multiple signs, and trees**, making it the perfect challenge for Rekognition’s labeling abilities.  

### **1️⃣ Creating the S3 Bucket**  
First, I created an **S3 bucket** named:  
🗂️ `aws-recognize-label`  
![S3 Bucket Setup](https://github.com/AaronG-Engineer/AWSRekognition/blob/main/pic%201.png)  

### **2️⃣ Uploading Images to Storage**  
I uploaded all **three images** to the S3 bucket for processing.  
![Image Uploads](https://github.com/AaronG-Engineer/AWSRekognition/blob/main/pic%202.png)  

### **3️⃣ Setting Up AWS CLI**  
To interact with AWS services from my terminal, I:  
✅ Installed AWS CLI  
✅ Checked setup with `aws --version`  
✅ Configured it using `aws configure`  
✅ Generated IAM access keys for authentication  
![AWS CLI Setup](https://github.com/AaronG-Engineer/AWSRekognition/blob/main/pic%203.png)  

### **4️⃣ Configuring My AWS User & Region**  
I ensured my AWS user was set up correctly, configured CLI with access keys, and matched the S3 bucket region. Then, it was time to **write the Python code!**  
![AWS User Configuration](https://github.com/AaronG-Engineer/AWSRekognition/blob/main/pic%204.png)  

### **5️⃣ Writing the Python Code & Importing Libraries**  
I set up my Python environment by creating a `.py` file in my IDE and installing the necessary libraries using pip.  
Then, I imported:  
🚀 `boto3` → AWS interactions  
🎨 `matplotlib` → Image visualization  
🖼️ `PIL` → Image handling  
📦 `BytesIO` → Efficient image processing  

### **6️⃣ Implementing `detect_labels` Function**  
I wrote a `detect_labels` function that:  
✅ Uses **Amazon Rekognition** to analyze an image from S3  
✅ Prints **labels with confidence scores**  
✅ Displays the image with **bounding boxes** for detected objects  

After that, I created a **main function** to test the system with a sample image and bucket name.  

### **7️⃣ Running the Python File & Viewing Results**  


![Final results!](https://github.com/AaronG-Engineer/AWSRekognition/blob/main/pic%205.png)

## 🔹 **Final Project Overview – System in Action**  
Below are the final four images showcasing different components of the image labeling system:  

🔹 **Top Screen:** The app processing an image and generating labels  
🔹 **Right Screen:** AI assistance analyzing objects  
🔹 **Left Section:** Code execution demonstrating bucket interaction  
🔹 **Bottom Section:** AWS storage structure for image processing  

![AWS User Configuration](https://github.com/AaronG-Engineer/AWSRekognition/blob/main/pic%206.png)  
