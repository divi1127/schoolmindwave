import os
import re

base_dir = r"c:\jod tech\mindwave-main"
template_path = os.path.join(base_dir, "blog-details.html")

with open(template_path, 'r', encoding='utf-8') as f:
    html = f.read()

video_placeholder = """                    <div class="tw-mb-8 rounded-4 overflow-hidden position-relative pb-video-container" style="background:#000; padding-bottom:56.25%; height:0;">
                        <!-- You can insert your YouTube iframe or video tag here. I put a placeholder style for right aspect ratio -->
                        <iframe id="blog-video" class="position-absolute top-0 start-0 w-100 h-100" src="" style="border:0;" allowfullscreen></iframe>
                        <div id="video-placeholder-text" class="text-white position-absolute top-50 start-50 translate-middle d-flex flex-column align-items-center">
                            <i class="ph-bold ph-video-camera text-main-600 mb-3" style="font-size: 48px;"></i>
                            <h4 class="text-white text-center">Video Will Go Here</h4>
                            <p class="text-white-50 text-center">Please provide the YouTube video URL</p>
                        </div>
                    </div>"""

def make_video_embed(url):
    return f"""                    <div class="tw-mb-8 d-flex justify-content-center">
                        <iframe src="{url}" width="400" height="480" frameborder="0" scrolling="no" allowtransparency="true"></iframe>
                    </div>"""

blogs_data = [
    {
        "id": 1,
        "title": "How to Prepare Your Child for Their First Day",
        "video": "https://www.instagram.com/reel/CxRUyfFh7Ue/embed/",
        "content": """
                    <div class="tw-text-4 text-paragraph-600 line-height-32-px">
                        <p class="tw-mb-5">
                            Preparing your child for their first day at a new learning center or school can feel overwhelming, but a few simple steps can make all the difference. Emphasizing routine and open communication ensures your child feels secure.
                        </p>
                        <p class="tw-mb-5">
                            Here at Mind Wave, we highly recommend establishing a morning routine weeks before the actual start date. This minimizes surprise and creates a sense of comfort and familiarity. Talk to your child positively about the fun activities, new friends, and caring teachers they will meet.
                        </p>
                        
                        <div class="bg-main-50 p-5 rounded-4 tw-mb-6 border-start border-4 border-main-600">
                            <h4 class="h5 fw-bold text-neutral-950 mb-3">Key Tips</h4>
                            <ul class="d-flex flex-column gap-2 mb-0">
                                <li><i class="ph-bold ph-check text-main-600 me-2"></i> Visit the center beforehand if possible.</li>
                                <li><i class="ph-bold ph-check text-main-600 me-2"></i> Establish consistent sleep and wake times.</li>
                                <li><i class="ph-bold ph-check text-main-600 me-2"></i> Validate their feelings regarding the new transition.</li>
                            </ul>
                        </div>

                        <p class="tw-mb-5">
                            Watch our reel above to see some direct insights from our experts on making the first day a gentle, positive experience for your child!
                        </p>
                    </div>"""
    },
    {
        "id": 2,
        "title": "Discovering the Joys of Child Kindergarten...",
        "video": "https://www.instagram.com/reel/DM0ZQeeSSff/embed/",
        "content": """
                    <div class="tw-text-4 text-paragraph-600 line-height-32-px">
                        <p class="tw-mb-5">
                            Early childhood education is fundamentally about discovery. When children step into a supportive environment tailored to their developmental needs, the joy of learning naturally blossoms.
                        </p>
                        <p class="tw-mb-5">
                            Play-based learning is at the heart of what we do at Mind Wave. Through carefully structured games, creative arts, and sensory activities, children develop critical thinking and problem-solving skills without even realizing it.
                        </p>
                        
                        <div class="bg-main-50 p-5 rounded-4 tw-mb-6 border-start border-4 border-main-600">
                            <h4 class="h5 fw-bold text-neutral-950 mb-3">Why Play Matters</h4>
                            <ul class="d-flex flex-column gap-2 mb-0">
                                <li><i class="ph-bold ph-check text-main-600 me-2"></i> Encourages natural curiosity and creativity.</li>
                                <li><i class="ph-bold ph-check text-main-600 me-2"></i> Helps toddlers process social interactions organically.</li>
                                <li><i class="ph-bold ph-check text-main-600 me-2"></i> Builds fine and gross motor skills.</li>
                            </ul>
                        </div>

                        <p class="tw-mb-5">
                            Check out the reel above to catch a glimpse of the daily joy, laughter, and learning happening right here in our discovery sessions!
                        </p>
                    </div>"""
    },
    {
        "id": 3,
        "title": "Creating Friendships and Memories in school...",
        "video": "https://www.instagram.com/reel/C2Sm55hvkiU/embed/",
        "content": """
                    <div class="tw-text-4 text-paragraph-600 line-height-32-px">
                        <p class="tw-mb-5">
                            Beyond academics and developmental milestones, school is the primary place where children learn to socialize, build empathy, and form their very first friendships.
                        </p>
                        <p class="tw-mb-5">
                            We actively foster environments where cooperative play and team-oriented activities are celebrated. Whether it's sharing toys, working together on an art project, or participating in group therapy, these moments are what construct lasting childhood memories.
                        </p>
                        
                        <div class="bg-main-50 p-5 rounded-4 tw-mb-6 border-start border-4 border-main-600">
                            <h4 class="h5 fw-bold text-neutral-950 mb-3">Fostering Connections</h4>
                            <ul class="d-flex flex-column gap-2 mb-0">
                                <li><i class="ph-bold ph-check text-main-600 me-2"></i> Group activities structured for inclusion.</li>
                                <li><i class="ph-bold ph-check text-main-600 me-2"></i> Guided lessons on sharing and emotional regulation.</li>
                                <li><i class="ph-bold ph-check text-main-600 me-2"></i> Celebrating teamwork and collective achievements.</li>
                            </ul>
                        </div>

                        <p class="tw-mb-5">
                            Watch the video above to see how our children interact, support one another, and build friendships that make everyday learning a collaborative adventure.
                        </p>
                    </div>"""
    }
]

for blog in blogs_data:
    new_html = html.replace(video_placeholder, make_video_embed(blog['video']))
    
    new_html = re.sub(r'<h2 class="h3 fw-bold text-neutral-950 tw-mb-6">.*?</h2>', f'<h2 class="h3 fw-bold text-neutral-950 tw-mb-6">{blog["title"]}</h2>', new_html, count=1, flags=re.DOTALL)
    
    new_html = re.sub(r'<!-- Blog Content -->.*?</article>', f'<!-- Blog Content -->\n{blog["content"]}\n                </article>', new_html, count=1, flags=re.DOTALL)
    
    other_blogs = [b for b in blogs_data if b['id'] != blog['id']]
    
    sidebar_replacement = f"""<!-- Recent Posts -->
                    <div class="widget bg-white shadow-sm p-4 rounded-4 tw-mb-6 border-top border-4 border-main-600">
                        <h4 class="h6 fw-bold text-neutral-950 tw-mb-4 border-bottom pb-3">Recent Articles</h4>
                        <ul class="d-flex flex-column gap-4 mb-0 list-unstyled">
                            <li class="d-flex align-items-center gap-3">
                                <img src="assets/images/thumbs/blog-img{other_blogs[0]['id']}.png" alt="img" class="rounded-3" style="width: 70px; height: 70px; object-fit: cover;">
                                <div>
                                    <h5 class="tw-text-405 fw-bold text-neutral-950 mb-1"><a href="blog-details-{other_blogs[0]['id']}.html" class="hover-text-main-600" style="transition: color 0.3s; color: inherit; text-decoration: none;">{other_blogs[0]['title'][:25]}...</a></h5>
                                </div>
                            </li>
                            <li class="d-flex align-items-center gap-3">
                                <img src="assets/images/thumbs/blog-img{other_blogs[1]['id']}.png" alt="img" class="rounded-3" style="width: 70px; height: 70px; object-fit: cover;">
                                <div>
                                    <h5 class="tw-text-405 fw-bold text-neutral-950 mb-1"><a href="blog-details-{other_blogs[1]['id']}.html" class="hover-text-main-600" style="transition: color 0.3s; color: inherit; text-decoration: none;">{other_blogs[1]['title'][:25]}...</a></h5>
                                </div>
                            </li>
                        </ul>
                    </div>

                    <!-- Contact/Promo Widget -->"""
    
    new_html = re.sub(r'<!-- Recent Posts -->.*?<!-- Contact/Promo Widget -->', sidebar_replacement, new_html, count=1, flags=re.DOTALL)
    
    with open(os.path.join(base_dir, f"blog-details-{blog['id']}.html"), 'w', encoding='utf-8') as f:
        f.write(new_html)

print("Created 3 blog detail pages successfully.")
