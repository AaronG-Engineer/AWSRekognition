def main():
    bucket_name = "your-s3-bucket"
    image_file = "sample-image.jpg"

    print(f"Processing image: {image_file} from bucket: {bucket_name}\n")

    label_count = analyze_image(image_file, bucket_name)

    print(f"Total labels detected: {label_count}")

if __name__ == "__main__":
    main()
# Code hidden due to private course restrictions
