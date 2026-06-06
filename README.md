# AgentOS
I'm Boumehdi abde ldjalil Hi, I'm a passionate programmer and web developer with expertise in front-end and back-end development. With a strong eye for design and a commitment to creating seamless user experiences, I specialize in crafting visually appealing and functional websites. Let's bring your ideas to life together!
AgentOS

AgentOS is an autonomous software engineering agent built with Python and FastAPI.

It is designed to analyze goals, generate project architectures, build applications, run tests, detect errors, and automatically apply fixes.

Features

- Autonomous task execution
- Project architecture generation
- Project compilation and code generation
- Automated testing
- Self-healing error recovery
- Memory system for task tracking
- FastAPI API interface
- Modular agent architecture
- Extensible tool system

Architecture

AgentOS
│
├── agents/
│   └── agent.py
│
├── core/
│   ├── architect.py
│   ├── compiler.py
│   ├── memory.py
│   ├── planner.py
│   ├── self_heal.py
│   └── tester.py
│
├── tools/
│   └── runner_tool.py
│
├── workspace/
│
└── main.py

Installation

Clone the repository:

git clone https://github.com/abdeldjalil-boumehdi/AgentOS.git
cd AgentOS

Create a virtual environment:

python -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Running AgentOS

Start the API server:

uvicorn main:app --host 127.0.0.1 --port 8000 --reload

Example Request

curl -X POST http://127.0.0.1:8000/task \
-H "Content-Type: application/json" \
-d '{"task":"build fastapi auth system"}'

Example Response

{
  "status": "AUTONOMOUS FACTORY COMPLETE"
}

Roadmap

- [ ] Multi-agent collaboration
- [ ] Automatic code refactoring
- [ ] GitHub integration
- [ ] Project deployment automation
- [ ] LLM-powered planning
- [ ] Cloud execution
- [ ] Docker support

License

MIT License

Author

Abdeldjalil Boumehdi
