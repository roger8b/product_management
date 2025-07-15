from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from pydantic import BaseModel, Field
from typing import List, Dict
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

from datetime import datetime

class ResearchPoint(BaseModel):
    topic: str = Field(description="The main topic or area being discussed")
    findings: str = Field(description="The key findings or insights about this topic")
    relevance: str = Field(description="Why this finding is relevant or important")
    sources: List[Dict[str, str]] = Field(
        description="Sources with title and URL for each finding",
        default_factory=list
    )

class ResearchOutput(BaseModel):
    research_points: List[ResearchPoint] = Field(description="List of research findings")
    summary: str = Field(description="Brief summary of overall findings")

def gerar_nome_arquivo(nome_base):
    return f"{nome_base}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

product_manager_knowledge = PDFKnowledgeSource(
    file_paths=["dicas_escrita_prd.pdf", "kit_ferramentas_prd.pdf", "modelo_prd.pdf"],
)

@CrewBase
class ProductManagement():
    """ProductManagement crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def product_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['product_manager'], # type: ignore[index]
            verbose=True,
            knowledge_sources=[product_manager_knowledge], # type: ignore[index]
        )
    

    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task'], # type: ignore[index]
            output_file=f"./result/{gerar_nome_arquivo('product_requirement_document')}"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ProductManagement crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            embedder={
                "provider": "ollama",
                "config": {
                    "model": "nomic-embed-text",
                    "base_url": "http://localhost:11434"
                }
            },
            
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
