import pygame
import sys
import random

pygame.init()

# Set up layar
lebar_layar = 600
tinggi_layar = 600
layar = pygame.display.set_mode((lebar_layar, tinggi_layar))
pygame.display.set_caption("Tangkap Bola")

# Warna
putih = (255, 255, 255)
hitam = (0, 0, 0)
merah = (255, 0, 0)
biru = (0, 0, 255)

# Font
font = pygame.font.SysFont(None, 36)

# Rakit pemain
rakit_lebar = 100
rakit_tinggi = 20
rakit = pygame.Surface((rakit_lebar, rakit_tinggi))
rakit.fill(merah)
posisi_rakit = [lebar_layar // 2 - rakit_lebar // 2, tinggi_layar - 2 * rakit_tinggi]

# Bola
bola_lebar = 20
bola_tinggi = 20
bola = pygame.Surface((bola_lebar, bola_tinggi))
bola.fill(biru)
posisi_bola = [random.randint(0, lebar_layar - bola_lebar), 0]
kecepatan_bola = 5

# Skor
skor = 0

# Kesempatan
kesempatan = 5

clock = pygame.time.Clock()

def game_over():
    teks_game_over = font.render(f"Game Over! Skor akhir: {skor}", True, hitam)
    layar.blit(teks_game_over, (lebar_layar // 2 - teks_game_over.get_width() // 2, tinggi_layar // 2 - teks_game_over.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(3000)

    # Tanyakan kepada pengguna apakah ingin bermain lagi
    pilihan = input("Apakah Anda ingin bermain lagi? (yes/no): ").lower()
    if pilihan == 'yes':
        reset_game()
    else:
        pygame.quit()
        sys.exit()

def reset_game():
    global posisi_bola, kecepatan_bola, skor, kesempatan
    posisi_bola = [random.randint(0, lebar_layar - bola_lebar), 0]
    kecepatan_bola = 5
    skor = 0
    kesempatan = 5

def main():
    global posisi_bola, kecepatan_bola, skor, kesempatan

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and posisi_rakit[0] > 0:
            posisi_rakit[0] -= 5
        if keys[pygame.K_RIGHT] and posisi_rakit[0] < lebar_layar - rakit_lebar:
            posisi_rakit[0] += 5

        # Pergerakan bola
        posisi_bola[1] += kecepatan_bola

        # Cek jika bola menyentuh rakit
        if posisi_bola[1] > tinggi_layar - 2 * rakit_tinggi and \
           posisi_rakit[0] < posisi_bola[0] < posisi_rakit[0] + rakit_lebar:
            posisi_bola = [random.randint(0, lebar_layar - bola_lebar), 0]
            kecepatan_bola += 1
            skor += 1

        # Cek jika bola melewati rakit
        if posisi_bola[1] > tinggi_layar:
            posisi_bola = [random.randint(0, lebar_layar - bola_lebar), 0]
            kecepatan_bola = 5
            kesempatan -= 1

        if kesempatan == 0:
            game_over()

        layar.fill(putih)
        layar.blit(rakit, posisi_rakit)
        layar.blit(bola, posisi_bola)

        # Tampilkan skor dan kesempatan
        teks_skor = font.render(f"Skor: {skor} | Kesempatan: {kesempatan}", True, hitam)
        layar.blit(teks_skor, (10, 10))

        pygame.display.flip()
        clock.tick(60)


pygame.init()


# Fungsi untuk menampilkan pertanyaan mau bermain lagi
def show_game_over_screen():
    font_big = pygame.font.SysFont(None, 72)
    text = font_big.render("Game Over", True, hitam)
    layar.blit(text, (lebar_layar // 2 - text.get_width() // 2, tinggi_layar // 4))

    font_small = pygame.font.SysFont(None, 36)
    text_score = font_small.render(f"Skor akhir: {skor}", True, hitam)
    layar.blit(text_score, (lebar_layar // 2 - text_score.get_width() // 2, tinggi_layar // 2))

    text_continue = font_small.render("Apakah Anda ingin bermain lagi? (y/n)", True, hitam)
    layar.blit(text_continue, (lebar_layar // 2 - text_continue.get_width() // 2, tinggi_layar // 1.5))

    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    waiting_for_input = False
                    reset_game()
                elif event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()


# tanya user mau bermain lagi
def game_over():
    show_game_over_screen()





if __name__ == "__main__":
    main()
