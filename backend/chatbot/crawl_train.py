from .crawler import crawl
from .trainer import train
from .status import STATUS
from tqdm import tqdm

def crawl_and_train(url):
    STATUS["running"] = True
    STATUS["pages"] = 0
    STATUS["chunks"] = 0

    print("\nCrawling website...\n")
    pages = crawl(url)

    print(f"\nFound {len(pages)} pages. Preparing chunks...\n")

    all_chunks = []

    # First pass — prepare all chunks
    for page in pages:
        STATUS["pages"] += 1
        chunks = [page[i:i+1000] for i in range(0, len(page), 1000)]
        for chunk in chunks:
            if len(chunk.strip()) > 50:
                all_chunks.append(chunk)

    total_chunks = len(all_chunks)
    print(f"Total chunks to train: {total_chunks}\n")

    # Second pass — real training with 100% progress bar
    bar = tqdm(total=total_chunks, desc="Training AI", ncols=100)

    for chunk in all_chunks:
        train(chunk)
        STATUS["chunks"] += 1

        percent = int((STATUS["chunks"] / total_chunks) * 100)
        bar.set_postfix({
            "Progress": f"{percent}%",
            "Chunks": f"{STATUS['chunks']}/{total_chunks}"
        })
        bar.update(1)

    bar.close()

    STATUS["running"] = False
    print("\nTraining completed successfully!\n")
