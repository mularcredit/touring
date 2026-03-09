const fs = require('fs');
const file = 'c:/Users/HomePC/Downloads/Touring/index.html';
let html = fs.readFileSync(file, 'utf8');

const modalHTML = `
<!-- Full Page Discover Modal (Book Style) -->
<div class="kz-discover-modal" id="discoverModal">
    <div class="kz-modal-close" id="modalClose">&times;</div>
    <div class="kz-modal-inner">
        <!-- Text Column -->
        <div class="kz-modal-text-col">
            <div class="kz-modal-badge" id="modalBadge">01</div>
            <h2 class="kz-modal-title" id="modalTitle">TITLE</h2>
            <div class="kz-modal-category-wrap">
                <i class="fas fa-map-marker-alt" style="color: #ff5e14; margin-right: 8px;"></i>
                <span class="kz-modal-category" id="modalCategory">Category</span>
            </div>
            
            <p class="kz-modal-desc" id="modalDesc">Description goes here...</p>
            
            <div class="kz-modal-elegant-note" id="modalNote">
                Crisp yet succulent premium experience capturing the essence of the wild.
            </div>

            <div class="kz-modal-price-box">
                <span class="price-label">Kaleola Zar Exclusive</span>
                <span class="price-val">Inquire Now</span>
            </div>

            <a href="#contact" class="kz-modal-book-btn" id="modalBookBtn" onclick="closeDiscoverModal()">Book Your Journey</a>
            <div style="margin-top:20px; font-size: 10px; color: #7b9986;">* All packages include premium accommodation and guided tours.</div>
        </div>
        
        <!-- Image Column -->
        <div class="kz-modal-image-col">
            <img id="modalImage" src="" alt="">
            <div class="kz-modal-image-badge">
                <span style="font-size: 10px; text-transform:uppercase; letter-spacing:1px; display:block; margin-bottom:2px; font-weight:700;">Top Choice</span>
                <strong style="font-size: 14px; font-family: Georgia, serif; font-style:italic;">Editor's Pick</strong>
                <div style="font-size: 8px; margin-top:4px; text-transform:uppercase; font-weight:700;">2026 Travel</div>
            </div>
            
            <!-- Floating Text Annotation (Mimicking the reference menu image lines) -->
            <div class="kz-modal-annotation" style="top: 20%; left: 10%;">
                <div class="annotation-text">Untouched wilderness</div>
                <div class="annotation-line" style="width: 40px; transform: rotate(15deg);"></div>
            </div>
            <div class="kz-modal-annotation" style="bottom: 30%; right: 15%;">
                <div class="annotation-text">Luxury camps</div>
                <div class="annotation-line" style="width: 50px; transform: rotate(-25deg); transform-origin: left center;"></div>
            </div>
        </div>
    </div>
</div>

<style>
    /* Full Page Modal Styles mimicking the Book Design */
    .kz-discover-modal {
        position: fixed;
        inset: 0;
        background: rgba(15, 25, 18, 0.95); /* Dark pine green backdrop */
        backdrop-filter: blur(10px);
        z-index: 99999;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        visibility: hidden;
        transition: all 0.5s cubic-bezier(0.25, 1, 0.5, 1);
        padding: 40px;
    }

    .kz-discover-modal.active {
        opacity: 1;
        visibility: visible;
    }

    .kz-modal-close {
        position: absolute;
        top: 30px;
        right: 40px;
        font-size: 50px;
        color: #fff;
        cursor: pointer;
        z-index: 2;
        transition: transform 0.3s ease, color 0.3s ease;
        line-height: 1;
        font-weight: 300;
    }
    
    .kz-modal-close:hover {
        transform: rotate(90deg);
        color: #ff5e14;
    }

    .kz-modal-inner {
        width: 100%;
        max-width: 1100px;
        height: 80vh;
        min-height: 600px;
        background: #193223; /* Exact book dark green color from the reference */
        border-radius: 4px;
        box-shadow: 0 30px 60px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(255,255,255,0.05);
        display: flex;
        overflow: hidden;
        transform: translateY(50px) scale(0.95);
        transition: all 0.6s cubic-bezier(0.25, 1, 0.5, 1) 0.1s;
    }

    .kz-discover-modal.active .kz-modal-inner {
        transform: translateY(0) scale(1);
    }

    .kz-modal-text-col {
        flex: 1;
        padding: 60px 50px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        position: relative;
    }

    .kz-modal-badge {
        width: 35px;
        height: 35px;
        background: #102116;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #fff;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-weight: 700;
        font-size: 12px;
        margin-bottom: 25px;
        border: 1px solid rgba(255,255,255,0.1);
        position: relative;
    }
    
    .kz-modal-badge::after {
        content: '';
        position: absolute;
        right: -30px;
        top: 50%;
        width: 20px;
        height: 1px;
        background: rgba(255,255,255,0.2);
    }

    .kz-modal-category-wrap {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }

    .kz-modal-category {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #ff5e14;
    }

    .kz-modal-title {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 42px;
        font-weight: 300;
        letter-spacing: 2px;
        color: #fff;
        margin: 0 0 20px;
        line-height: 1.1;
        text-transform: uppercase;
    }

    .kz-modal-title strong {
        font-weight: 700;
        color: #fff;
    }

    .kz-modal-desc {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 15px;
        font-weight: 300;
        color: #c4d4ca;
        line-height: 1.8;
        margin-bottom: 30px;
        max-width: 400px;
    }

    .kz-modal-elegant-note {
        font-family: 'Caveat', Georgia, 'Playfair Display', cursive, serif;
        font-style: italic;
        font-size: 24px;
        color: #e5f0ea;
        margin-bottom: 40px;
        line-height: 1.3;
        position: relative;
        padding-left: 0;
    }

    .kz-modal-price-box {
        margin-bottom: 30px;
        padding-top: 20px;
        border-top: 1px solid rgba(255,255,255,0.1);
        display: inline-block;
        min-width: 200px;
    }
    .kz-modal-price-box .price-label {
        display: block;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #7b9986;
        margin-bottom: 5px;
    }
    .kz-modal-price-box .price-val {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 18px;
        font-weight: 600;
        color: #fff;
    }

    .kz-modal-book-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 16px 36px;
        background: #ff5e14;
        color: #fff;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 3px;
        text-transform: uppercase;
        border-radius: 4px; /* Flatter button to match editorial look */
        text-decoration: none;
        transition: all 0.3s ease;
        align-self: flex-start;
        border: 1px solid transparent;
    }

    .kz-modal-book-btn:hover {
        background: transparent;
        color: #ff5e14;
        border-color: #ff5e14;
    }

    .kz-modal-image-col {
        flex: 1.2;
        position: relative;
        background: #111;
        overflow: hidden;
        border-left: 1px solid rgba(0,0,0,0.2); /* Mimic page fold */
        box-shadow: inset 10px 0 20px -10px rgba(0,0,0,0.5); /* Book gutter shadow */
    }

    .kz-modal-image-col img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        opacity: 0.95;
        transition: transform 1s cubic-bezier(0.25, 1, 0.5, 1);
    }
    
    .kz-discover-modal.active .kz-modal-image-col img {
        transform: scale(1.03); /* Slow zoom in when opened */
    }

    /* Small decorative badge over image like CNN Travel badge in the reference */
    .kz-modal-image-badge {
        position: absolute;
        top: 30px;
        right: 30px;
        background: #d99a2c; /* The distinct yellow/orange from the reference photo */
        color: #fff;
        padding: 12px 15px;
        text-align: center;
        font-family: 'Plus Jakarta Sans', sans-serif;
        border-radius: 2px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        z-index: 2;
    }
    
    /* Handwritten annotations pointing to the image */
    .kz-modal-annotation {
        position: absolute;
        color: #fff;
        z-index: 2;
        opacity: 0;
        transform: translateY(10px);
        transition: all 0.8s ease 0.5s;
    }
    
    .kz-discover-modal.active .kz-modal-annotation {
        opacity: 1;
        transform: translateY(0);
    }
    
    .kz-modal-annotation .annotation-text {
        font-family: 'Caveat', Georgia, 'Playfair Display', cursive, serif;
        font-style: italic;
        font-size: 16px;
        margin-bottom: 5px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
    }
    
    .kz-modal-annotation .annotation-line {
        height: 1px;
        background: #fff;
        box-shadow: 0 1px 2px rgba(0,0,0,0.5);
    }

    @media (max-width: 991px) {
        .kz-modal-inner {
            flex-direction: column-reverse;
            height: 90vh;
            overflow-y: auto;
        }
        .kz-modal-text-col {
            padding: 40px 30px;
            overflow-y: visible;
        }
        .kz-modal-image-col {
            min-height: 300px;
            flex: none;
        }
        .kz-modal-title {
            font-size: 32px;
        }
        .kz-modal-elegant-note {
            font-size: 20px;
        }
        .kz-modal-image-badge {
            top: 15px;
            right: 15px;
        }
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', function() {
        // Find Modal Elements
        const modal = document.getElementById('discoverModal');
        const closeBtn = document.getElementById('modalClose');
        const mTitle = document.getElementById('modalTitle');
        const mCategory = document.getElementById('modalCategory');
        const mDesc = document.getElementById('modalDesc');
        const mImage = document.getElementById('modalImage');
        const mBadge = document.getElementById('modalBadge');

        if(!modal) return;

        // Attach click events to grid items
        const gridItems = document.querySelectorAll('.kz-grid-item');
        
        gridItems.forEach((item, index) => {
            item.addEventListener('click', function(e) {
                // Prevent scrolling to #contact instantly when clicking card
                e.preventDefault();
                
                // Extract data from the clicked card
                const catNode = this.querySelector('.kz-grid-category');
                const titleNode = this.querySelector('.kz-grid-title');
                const descNode = this.querySelector('.kz-grid-desc');
                const imgNode = this.querySelector('.kz-grid-img');

                if(!titleNode || !imgNode) return;

                const cat = catNode ? catNode.innerText : 'Destination';
                const title = titleNode.innerText;
                const desc = descNode ? descNode.innerText : '';
                const imgSrc = imgNode.src;
                
                // Populate Modal mimicking the editorial style
                mBadge.innerText = String(index + 421); // Fun detail mapping to the "421" "422" numbers on the menu image
                mCategory.innerText = cat;
                
                // Highlight the first word if it contains multiple words
                let words = title.split(' ');
                if(words.length > 1) {
                    mTitle.innerHTML = '<strong>' + words[0] + '</strong><br>' + words.slice(1).join(' ');
                } else {
                    mTitle.innerHTML = '<strong>' + title + '</strong>';
                }

                mDesc.innerText = "Experience the breathtaking beauty of " + title + ". " + desc + " awaits you with an unforgettable adventure. Immerse yourself in the rich culture and stunning landscapes.";
                mImage.src = imgSrc;
                
                // Show modal
                modal.classList.add('active');
                document.body.style.overflow = 'hidden'; // Stop background scrolling
            });
        });

        // Close functions
        const closeModal = function() {
            modal.classList.remove('active');
            document.body.style.overflow = '';
        };

        if(closeBtn) {
            closeBtn.addEventListener('click', closeModal);
        }
        
        // Close on outside click
        modal.addEventListener('click', function(e) {
            if(e.target === modal) {
                closeModal();
            }
        });
        
        // Close on ESC key
        document.addEventListener('keydown', function(e) {
            if(e.key === 'Escape') {
                closeModal();
            }
        });
    });

    // Make global for book now button click
    window.closeDiscoverModal = function() {
        const modal = document.getElementById('discoverModal');
        modal.classList.remove('active');
        document.body.style.overflow = '';
    }
</script>
`;

if (!html.includes('id="discoverModal"')) {
    html = html.replace('</body>', modalHTML + '\n</body>');
    fs.writeFileSync(file, html, 'utf8');
    console.log('Successfully injected Discover Modal.');
} else {
    // If we've run it before, just replace the existing modal block
    const regex = /<!-- Full Page Discover Modal.*?<\/script>/s;
    if (html.match(regex)) {
        html = html.replace(regex, modalHTML);
        fs.writeFileSync(file, html, 'utf8');
        console.log('Successfully updated Discover Modal.');
    } else {
        console.log('Modal exists but replace failed.');
    }
}
