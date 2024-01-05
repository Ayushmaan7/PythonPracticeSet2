import re

def analyze_social_media_post(post):
    # Count the number of words in the post
    words = post.split()
    word_count = len(words)

    # Find hashtags in the post
    hashtags = re.findall(r'#\w+', post)

    return word_count, hashtags

if __name__ == "__main__":
    social_media_post = input("Enter a social media post: ")

    # Analyze the social media post
    num_words, post_hashtags = analyze_social_media_post(social_media_post)

    # Display the analysis results
    print(f"Number of words in the post: {num_words}")
    
    if post_hashtags:
        print("Hashtags found in the post:")
        for hashtag in post_hashtags:
            print(hashtag)
    else:
        print("No hashtags found in the post.")
