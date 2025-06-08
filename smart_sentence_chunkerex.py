import re

class SmartSentenceChunkerex:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "long_text": ("STRING", {"multiline": True}),
                "min_chunk_length": ("INT", {"default": 300, "min": 10, "max": 1000}),
            }
        }

    RETURN_TYPES = tuple(["STRING"] * 20)
    RETURN_NAMES = tuple([f"text_{chr(97 + i)}" for i in range(20)])  # text_a to text_t
    FUNCTION = "split_text"
    CATEGORY = "text"

    def split_text(self, long_text, min_chunk_length):
        # Split into sentences
        sentences = re.split(r'(?<=[.!?"])\s+', long_text.strip())

        chunks = []
        current_chunk = ""

        for sentence in sentences:
            tentative = f"{current_chunk} {sentence}".strip() if current_chunk else sentence

            if len(tentative) < min_chunk_length:
                current_chunk = tentative
            else:
                chunks.append(tentative.strip())
                current_chunk = ""

        if current_chunk:
            chunks.append(current_chunk.strip())

        # Pad to 20 outputs
        padded_chunks = chunks[:20] + [""] * (20 - len(chunks))
        return tuple(padded_chunks)


NODE_CLASS_MAPPINGS = {
    "SmartSentenceChunkerex": SmartSentenceChunkerex,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SmartSentenceChunkerex": "Text → Sentence Chunks A–T",
}
