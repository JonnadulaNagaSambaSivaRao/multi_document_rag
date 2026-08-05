from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def build_chain(llm, db):

    retriever = db.as_retriever(
        search_kwargs={"k":3}
    )

    prompt = ChatPromptTemplate.from_template(
        """
Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""
    )

    def ask(question):

        docs = retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        answer = (
            prompt
            | llm
            | StrOutputParser()
        ).invoke(
            {
                "context": context,
                "question": question,
            }
        )

        return {
            "answer": answer,
            "documents": docs,
        }

    return ask