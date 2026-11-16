import tkinter as tk
from tkinter import messagebox
import random

class JuegoPiedraPapelTijera:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego: Piedra, Papel o Tijera")
        self.root.geometry("520x640")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        # Variables de puntuación
        self.puntos_jugador = 0
        self.puntos_maquina = 0
        self.empates = 0
        self.animando = False

        # Datos de las jugadas: (Nombre, Emoji)
        self.opciones = {
            "piedra": {"nombre": "Piedra", "emoji": "🪨"},
            "papel": {"nombre": "Papel", "emoji": "📄"},
            "tijera": {"nombre": "Tijera", "emoji": "✂️"}
        }

        self.crear_interfaz()

    def crear_interfaz(self):
        # --- TÍTULO ---
        frame_titulo = tk.Frame(self.root, bg="#1e1e2e")
        frame_titulo.pack(pady=(20, 10))

        lbl_titulo = tk.Label(
            frame_titulo,
            text="PIEDRA, PAPEL O TIJERA",
            font=("Segoe UI", 20, "bold"),
            fg="#cdd6f4",
            bg="#1e1e2e"
        )
        lbl_titulo.pack()

        lbl_subtitulo = tk.Label(
            frame_titulo,
            text="¡Elige tu jugada para desafiar a la máquina!",
            font=("Segoe UI", 11),
            fg="#a6adc8",
            bg="#1e1e2e"
        )
        lbl_subtitulo.pack(pady=4)

        # --- MARCADOR ---
        frame_marcador = tk.Frame(self.root, bg="#313244", bd=0, relief="ridge")
        frame_marcador.pack(padx=25, pady=10, fill="x")

        # Columnas del marcador
        self.lbl_puntos_jugador = tk.Label(
            frame_marcador,
            text="Tú: 0",
            font=("Segoe UI", 14, "bold"),
            fg="#a6e3a1",
            bg="#313244",
            width=12,
            pady=10
        )
        self.lbl_puntos_jugador.grid(row=0, column=0, sticky="nsew")

        self.lbl_empates = tk.Label(
            frame_marcador,
            text="Empates: 0",
            font=("Segoe UI", 13),
            fg="#f9e2af",
            bg="#313244",
            width=12,
            pady=10
        )
        self.lbl_empates.grid(row=0, column=1, sticky="nsew")

        self.lbl_puntos_maquina = tk.Label(
            frame_marcador,
            text="Máquina: 0",
            font=("Segoe UI", 14, "bold"),
            fg="#f38ba8",
            bg="#313244",
            width=12,
            pady=10
        )
        self.lbl_puntos_maquina.grid(row=0, column=2, sticky="nsew")

        frame_marcador.columnconfigure(0, weight=1)
        frame_marcador.columnconfigure(1, weight=1)
        frame_marcador.columnconfigure(2, weight=1)

        # --- TABLERO DE ENFRENTAMIENTO (DUELO) ---
        frame_duelo = tk.Frame(self.root, bg="#181825", bd=2, relief="groove")
        frame_duelo.pack(padx=25, pady=15, fill="both", expand=True)

        # Jugador
        frame_izq = tk.Frame(frame_duelo, bg="#181825")
        frame_izq.pack(side="left", expand=True, fill="both", pady=15)

        lbl_tag_jugador = tk.Label(frame_izq, text="TU JUGADA", font=("Segoe UI", 10, "bold"), fg="#89b4fa", bg="#181825")
        lbl_tag_jugador.pack()
        self.lbl_emoji_jugador = tk.Label(frame_izq, text="❓", font=("Segoe UI Emoji", 55), fg="#cdd6f4", bg="#181825")
        self.lbl_emoji_jugador.pack(pady=5)
        self.lbl_texto_jugador = tk.Label(frame_izq, text="-", font=("Segoe UI", 12), fg="#a6adc8", bg="#181825")
        self.lbl_texto_jugador.pack()

        # Separador VS
        lbl_vs = tk.Label(frame_duelo, text="VS", font=("Segoe UI", 18, "bold"), fg="#fab387", bg="#181825")
        lbl_vs.pack(side="left", padx=5)

        # Computadora
        frame_der = tk.Frame(frame_duelo, bg="#181825")
        frame_der.pack(side="right", expand=True, fill="both", pady=15)

        lbl_tag_maquina = tk.Label(frame_der, text="COMPUTADORA", font=("Segoe UI", 10, "bold"), fg="#f38ba8", bg="#181825")
        lbl_tag_maquina.pack()
        self.lbl_emoji_maquina = tk.Label(frame_der, text="❓", font=("Segoe UI Emoji", 55), fg="#cdd6f4", bg="#181825")
        self.lbl_emoji_maquina.pack(pady=5)
        self.lbl_texto_maquina = tk.Label(frame_der, text="-", font=("Segoe UI", 12), fg="#a6adc8", bg="#181825")
        self.lbl_texto_maquina.pack()

        # --- MENSAJE DE RESULTADO ---
        self.lbl_resultado = tk.Label(
            self.root,
            text="Selecciona Piedra, Papel o Tijera abajo 👇",
            font=("Segoe UI", 13, "bold"),
            fg="#cdd6f4",
            bg="#1e1e2e",
            wraplength=460,
            pady=8
        )
        self.lbl_resultado.pack(pady=(5, 10))

        # --- BOTONES DE ELECCIÓN ---
        frame_botones = tk.Frame(self.root, bg="#1e1e2e")
        frame_botones.pack(pady=10)

        self.btn_piedra = self.crear_boton_jugada(frame_botones, "🪨 Piedra", "piedra", "#45475a", "#585b70")
        self.btn_piedra.grid(row=0, column=0, padx=8)

        self.btn_papel = self.crear_boton_jugada(frame_botones, "📄 Papel", "papel", "#45475a", "#585b70")
        self.btn_papel.grid(row=0, column=1, padx=8)

        self.btn_tijera = self.crear_boton_jugada(frame_botones, "✂️ Tijera", "tijera", "#45475a", "#585b70")
        self.btn_tijera.grid(row=0, column=2, padx=8)

        self.botones_juego = [self.btn_piedra, self.btn_papel, self.btn_tijera]

        # --- BOTONES DE CONTROL (REINICIAR / SALIR) ---
        frame_controles = tk.Frame(self.root, bg="#1e1e2e")
        frame_controles.pack(side="bottom", pady=20)

        btn_reiniciar = tk.Button(
            frame_controles,
            text="🔄 Reiniciar Marcador",
            font=("Segoe UI", 10),
            bg="#313244",
            fg="#cdd6f4",
            activebackground="#45475a",
            activeforeground="#ffffff",
            bd=0,
            padx=14,
            pady=6,
            cursor="hand2",
            command=self.reiniciar_juego
        )
        btn_reiniciar.grid(row=0, column=0, padx=10)

        btn_salir = tk.Button(
            frame_controles,
            text="❌ Salir",
            font=("Segoe UI", 10),
            bg="#313244",
            fg="#f38ba8",
            activebackground="#45475a",
            activeforeground="#ffffff",
            bd=0,
            padx=16,
            pady=6,
            cursor="hand2",
            command=self.root.quit
        )
        btn_salir.grid(row=0, column=1, padx=10)

    def crear_boton_jugada(self, padre, texto, jugada, color_bg, color_hover):
        btn = tk.Button(
            padre,
            text=texto,
            font=("Segoe UI", 12, "bold"),
            bg=color_bg,
            fg="#ffffff",
            activebackground=color_hover,
            activeforeground="#ffffff",
            bd=0,
            padx=16,
            pady=12,
            cursor="hand2",
            width=9,
            command=lambda: self.jugar(jugada)
        )
        # Efecto hover al pasar el ratón
        btn.bind("<Enter>", lambda e: btn.config(bg=color_hover))
        btn.bind("<Leave>", lambda e: btn.config(bg=color_bg))
        return btn

    def animar_rueda(self, frames_restantes, eleccion_jugador, callback_final):
        """Pequeña animación de suspenso antes de mostrar el resultado final"""
        if frames_restantes > 0:
            emojis_anim = ["🪨", "📄", "✂️"]
            emoji_random = random.choice(emojis_anim)
            self.lbl_emoji_maquina.config(text=emoji_random)
            self.lbl_texto_maquina.config(text="Pensando...")
            self.root.after(100, lambda: self.animar_rueda(frames_restantes - 1, eleccion_jugador, callback_final))
        else:
            callback_final()

    def jugar(self, eleccion_jugador):
        if self.animando:
            return

        self.animando = True
        for btn in self.botones_juego:
            btn.config(state="disabled")

        # Mostrar elección del jugador de inmediato
        datos_jugador = self.opciones[eleccion_jugador]
        self.lbl_emoji_jugador.config(text=datos_jugador["emoji"])
        self.lbl_texto_jugador.config(text=datos_jugador["nombre"])
        self.lbl_resultado.config(text="La computadora está eligiendo...", fg="#fab387")

        # Iniciar animación y resolución
        def resolver():
            eleccion_maquina = random.choice(["piedra", "papel", "tijera"])
            datos_maquina = self.opciones[eleccion_maquina]

            self.lbl_emoji_maquina.config(text=datos_maquina["emoji"])
            self.lbl_texto_maquina.config(text=datos_maquina["nombre"])

            # Comprobar resultado
            if eleccion_jugador == eleccion_maquina:
                self.empates += 1
                self.lbl_resultado.config(text="🤝 ¡Empate! Ambos eligieron lo mismo.", fg="#f9e2af")
            elif (eleccion_jugador == "piedra" and eleccion_maquina == "tijera") or \
                 (eleccion_jugador == "papel" and eleccion_maquina == "piedra") or \
                 (eleccion_jugador == "tijera" and eleccion_maquina == "papel"):
                self.puntos_jugador += 1
                self.lbl_resultado.config(text=f"🎉 ¡Ganaste! {datos_jugador['nombre']} vence a {datos_maquina['nombre']}.", fg="#a6e3a1")
            else:
                self.puntos_maquina += 1
                self.lbl_resultado.config(text=f"😢 Perdiste. {datos_maquina['nombre']} vence a {datos_jugador['nombre']}.", fg="#f38ba8")

            # Actualizar textos del marcador
            self.lbl_puntos_jugador.config(text=f"Tú: {self.puntos_jugador}")
            self.lbl_empates.config(text=f"Empates: {self.empates}")
            self.lbl_puntos_maquina.config(text=f"Máquina: {self.puntos_maquina}")

            # Reactivar botones
            for btn in self.botones_juego:
                btn.config(state="normal")
            self.animando = False

        self.animar_rueda(5, eleccion_jugador, resolver)

    def reiniciar_juego(self):
        if messagebox.askyesno("Reiniciar", "¿Estás seguro/a de que quieres reiniciar el marcador?"):
            self.puntos_jugador = 0
            self.puntos_maquina = 0
            self.empates = 0
            self.lbl_puntos_jugador.config(text="Tú: 0")
            self.lbl_empates.config(text="Empates: 0")
            self.lbl_puntos_maquina.config(text="Máquina: 0")
            self.lbl_emoji_jugador.config(text="❓")
            self.lbl_texto_jugador.config(text="-")
            self.lbl_emoji_maquina.config(text="❓")
            self.lbl_texto_maquina.config(text="-")
            self.lbl_resultado.config(text="Marcador reiniciado. ¡Elige tu jugada!", fg="#cdd6f4")


def main():
    root = tk.Tk()
    app = JuegoPiedraPapelTijera(root)
    root.mainloop()

if __name__ == "__main__":
    main()
