import streamlit as st
from transformers import AutoTokenizer
import torch


# Cache the tokenizer to avoid reloading
@st.cache_resource
def load_tokenizer(model_name):
    """Load and cache the tokenizer"""
    try:
        return AutoTokenizer.from_pretrained(model_name)
    except Exception as e:
        st.error(f"Error loading tokenizer: {str(e)}")
        return None


def show_tokenizers():
    """Display the tokenizers demo page"""

    st.title("🔤 Text Tokenizers Demo")
    st.markdown("---")

    st.markdown("""
    This page demonstrates how different tokenizers break down text into tokens.
    Tokenization is a crucial step in natural language processing where text is converted
    into numerical representations that machine learning models can understand.
    """)

    # Sidebar for model selection
    st.sidebar.header("Tokenizer Settings")

    # Model selection
    model_options = {
        "BERT (bert-base-uncased)": "bert-base-uncased",
        "GPT-2 (gpt2)": "gpt2",
        "RoBERTa (roberta-base)": "roberta-base",
        "DistilBERT (distilbert-base-uncased)": "distilbert-base-uncased",
    }

    selected_model = st.sidebar.selectbox("Choose a tokenizer model:", list(model_options.keys()))

    model_name = model_options[selected_model]

    # Load tokenizer
    with st.spinner(f"Loading {selected_model} tokenizer..."):
        tokenizer = load_tokenizer(model_name)

    if tokenizer is None:
        st.error("Failed to load tokenizer. Please try another model.")
        return

    st.success(f"✅ {selected_model} tokenizer loaded successfully!")

    # Text input section
    st.header("📝 Text Input")

    # Default example text
    default_text = "Hello world! This is a sample text for tokenization. How does the tokenizer handle punctuation, numbers like 123, and special characters?"

    input_text = st.text_area(
        "Enter your text to tokenize:",
        value=default_text,
        height=100,
        help="Enter any text you'd like to see tokenized. Try different types of content!",
    )

    if input_text.strip():
        # Tokenization
        with st.spinner("Tokenizing text..."):
            try:
                # Tokenize the input
                tokens = tokenizer.tokenize(input_text)
                token_ids = tokenizer.encode(input_text)
                decoded_text = tokenizer.decode(token_ids)

            except Exception as e:
                st.error(f"Error during tokenization: {str(e)}")
                return

        # Display results
        st.header("🧩 Tokenization Results")

        # Create tabs for different views
        tab1, tab2, tab3, tab4 = st.tabs(["Tokens", "Token IDs", "Decoded Text", "Statistics"])

        with tab1:
            st.subheader("Text Tokens")
            st.markdown("Here's how the text is broken down into tokens:")

            # Display tokens with highlighting
            token_html = ""
            colors = ["#FFE6E6", "#E6F3FF", "#E6FFE6", "#FFF0E6", "#F0E6FF", "#E6FFFF"]

            for i, token in enumerate(tokens):
                color = colors[i % len(colors)]
                # Escape HTML and handle special tokens
                display_token = token.replace("<", "&lt;").replace(">", "&gt;")
                token_html += f'<span style="background-color: {color}; padding: 2px 4px; margin: 1px; border-radius: 3px; font-family: monospace;">{display_token}</span> '

            st.markdown(token_html, unsafe_allow_html=True)

            st.markdown("**Token List:**")
            for i, token in enumerate(tokens, 1):
                st.write(f"{i:2d}. `{token}`")

        with tab2:
            st.subheader("Token IDs")
            st.markdown("Each token is converted to a numerical ID:")

            # Display token IDs
            st.code(str(token_ids))

            # Display mapping
            st.markdown("**Token → ID Mapping:**")
            for token, token_id in zip(tokens, token_ids[1:-1] if len(token_ids) > len(tokens) else token_ids):
                st.write(f"`{token}` → `{token_id}`")

        with tab3:
            st.subheader("Decoded Text")
            st.markdown("Text reconstructed from token IDs:")
            st.text_area("Decoded:", value=decoded_text, height=100, disabled=True)

            # Check if decoding is lossless
            if decoded_text.strip() == input_text.strip():
                st.success("✅ Lossless encoding/decoding")
            else:
                st.warning("⚠️ Some information was lost in encoding/decoding")

        with tab4:
            st.subheader("Tokenization Statistics")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Original Characters", len(input_text))

            with col2:
                st.metric("Number of Tokens", len(tokens))

            with col3:
                compression_ratio = len(input_text) / len(tokens) if tokens else 0
                st.metric("Chars per Token", f"{compression_ratio:.2f}")

            # Additional stats
            st.markdown("**Additional Information:**")
            st.write(f"- Vocabulary size: {tokenizer.vocab_size:,}")
            st.write(f"- Model max length: {tokenizer.model_max_length:,}")
            st.write(f"- Special tokens: {len(tokenizer.special_tokens_map)}")

            if hasattr(tokenizer, "unk_token") and tokenizer.unk_token:
                st.write(f"- Unknown token: `{tokenizer.unk_token}`")
            if hasattr(tokenizer, "pad_token") and tokenizer.pad_token:
                st.write(f"- Padding token: `{tokenizer.pad_token}`")

    else:
        st.info("👆 Enter some text above to see how it gets tokenized!")

    # Educational section
    st.markdown("---")
    st.header("📚 About Tokenization")

    with st.expander("What is tokenization?"):
        st.markdown("""
        **Tokenization** is the process of converting text into smaller units called tokens.
        These tokens can be words, subwords, or even characters, depending on the tokenization strategy.

        **Why is it important?**
        - Machine learning models work with numbers, not text
        - Tokenization bridges the gap between human language and machine understanding
        - Different tokenization strategies affect model performance and capabilities
        """)

    with st.expander("Different tokenization approaches"):
        st.markdown("""
        **Word-level tokenization**: Splits text into whole words
        - Pro: Intuitive and preserves word meaning
        - Con: Large vocabulary, struggles with out-of-vocabulary words

        **Subword tokenization**: Splits text into smaller units than words
        - **BPE (Byte Pair Encoding)**: Used by GPT models
        - **WordPiece**: Used by BERT models
        - **SentencePiece**: Used by T5 and other models

        **Character-level tokenization**: Each character is a token
        - Pro: No out-of-vocabulary issues, small vocabulary
        - Con: Long sequences, harder to capture meaning
        """)

    # Navigation back to home
    st.markdown("---")
    if st.button("← Back to Portfolio"):
        st.switch_page("app.py")
