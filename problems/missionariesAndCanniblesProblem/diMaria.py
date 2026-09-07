# Author: Di Maria Matteo

class MissionariesProblem:
    def __init__(self, initial_state=(3, 3, 1), goal_state=(0, 0, 0)):
        """
        Stato: (M_sinistra, C_sinistra, Barca)
        Barca: 1 = Sinistra, 0 = Destra
        """
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.capacity = 2 # Capacità barca

    def is_safe(self, m, c):
        """
        Controllo se una sponda con m missionari e c cannibali è sicura.
        Regola: I missionari non devono essere in minoranza MA solo se sono presenti.
        """
        if m < 0 or c < 0 or m > 3 or c > 3:
            return False # Limiti fisici superati
        if m == 0:
            return True # Se non ci sono missionari, sono tutti al sicuro
        return m >= c # Se ci sono, devono essere >= dei cannibali

    def actions(self, state):
        """
        Genera le azioni che non portano a uno stato illegale.
        """
        m_left, c_left, boat = state
        valid_actions = []

        # Generiamo tutte le combinazioni possibili di persone sulla barca (m, c)
        # x = missionari sulla barca, y = cannibali sulla barca
        for x in range(self.capacity + 1):
            for y in range(self.capacity + 1 - x):
                if x == 0 and y == 0:
                    continue # La barca non può viaggiare vuota

                # Calcoliamo lo stato ipotetico dopo lo spostamento
                if boat == 1: # Barca va da Sinistra a Destra (Sottraggo)
                    new_m_left, new_c_left = m_left - x, c_left - y
                    new_boat = 0
                else: # Barca va da Destra a Sinistra (Aggiungo)
                    new_m_left, new_c_left = m_left + x, c_left + y
                    new_boat = 1

                # Calcoliamo quanti sono a destra (Totale - Sinistra)
                m_right, c_right = 3 - new_m_left, 3 - new_c_left

                # Applichiamo i filtri di sicurezza
                if self.is_safe(new_m_left, new_c_left) and self.is_safe(m_right, c_right):
                    valid_actions.append((x, y))

        return valid_actions

    def result(self, state, action):
        """Esegue fisicamente lo spostamento"""
        m_left, c_left, boat = state
        m_boat, c_boat = action

        if boat == 1:
            return (m_left - m_boat, c_left - c_boat, 0)
        else:
            return (m_left + m_boat, c_left + c_boat, 1)

    def action_cost(self, state, action):
        return 1

    def is_goal(self, state):
        return state == self.goal_state

    def heuristic(self, state):
        """Numero di persone ancora sulla sponda sinistra"""
        return state[0] + state[1]