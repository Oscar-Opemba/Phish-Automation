from app.simulator import Simulator
from app.metrics import risk_score

def main():
    sim = Simulator()
    events = sim.run()
    print("Synthetic events:", events)
    print("Risk score:", risk_score(events))

if __name__ == "__main__":
    main()
