import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;
import javax.sound.sampled.*;
import java.io.File;
import java.io.IOException;

public class GameLauncher {

    // Constants
    private static final int SCREEN_WIDTH = 820;
    private static final int SCREEN_HEIGHT = 300;

    // Colors
    private static final Color WHITE = new Color(255, 255, 255);
    private static final Color BLACK = new Color(0, 0, 0);
    private static final Color GRAY = new Color(200, 200, 200);
    private static final Color GREEN = new Color(0, 255, 0);

    private static final String[] GAME_NAMES = {
        "1. Snake",
        "2. Flappy Bird",
        "3. GUI Calculator",
        "4. Slide Puzzle",
        "5. Space Invaders",
        "6. SnowFall",
        "7. Auto Tic Tac Toe",
        "8. Manual Tic Tac Toe"
    };

    private JFrame frame;
    private JPanel panel;
    private JButton[] buttons;
    private Color[] targetButtonColorsRed;
    private Color[] targetButtonColorsGreen;
    private Color[] targetButtonColorsBlue;
    private Color[] buttonColorsRed;
    private Color[] buttonColorsGreen;
    private Color[] buttonColorsBlue;
    private Clip musicClip;
    private int hoveringButton = 0;
    private int previousHoveringButton = 0;

    private double yScroll = 0;
    private double yScrollVelocity = 0;
    private long startTime;
    private double deltaTime = 0.0001;
    private double gameTime = -0.0001;

    public GameLauncher() {
        initializeMusic();
        initializeUI();
        startGameLoop();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new GameLauncher());
    }

    private void initializeMusic() {
        PlayMusic(new Random().nextInt(2) + 1);
    }

    private void PlayMusic(int musNum) {
        try {
            if (musNum == 1) {
                File musicPath = new File("GameLauncher/assets/audio/Debug Menu Unused   Paper Mario  The Thousand Year Door.wav");
                if (musicPath.exists()) {
                    AudioInputStream audioInput = AudioSystem.getAudioInputStream(musicPath);
                    musicClip = AudioSystem.getClip();
                    musicClip.open(audioInput);
                    musicClip.loop(Clip.LOOP_CONTINUOUSLY);
                }
            } else if (musNum == 2) {
                File musicPath = new File("GameLauncher/assets/audio/SpongeBob SquarePants OST - Dombummel (LQ).wav");
                if (musicPath.exists()) {
                    AudioInputStream audioInput = AudioSystem.getAudioInputStream(musicPath);
                    musicClip = AudioSystem.getClip();
                    musicClip.open(audioInput);
                    musicClip.loop(Clip.LOOP_CONTINUOUSLY);
                }
            }
        } catch (UnsupportedAudioFileException | IOException | LineUnavailableException e) {
            e.printStackTrace();
        }
    }

    private void initializeUI() {
        frame = new JFrame("Game Launcher");
        frame.setSize(SCREEN_WIDTH, SCREEN_HEIGHT);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setResizable(true);

        panel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                drawBackground(g);
                drawButtons(g);
            }
        };
        panel.setLayout(null);
        frame.add(panel);

        initializeButtons();

        frame.setVisible(true);
    }

    private void initializeButtons() {
        buttons = new JButton[GAME_NAMES.length];
        buttonColorsRed = new Color[GAME_NAMES.length];
        buttonColorsGreen = new Color[GAME_NAMES.length];
        buttonColorsBlue = new Color[GAME_NAMES.length];
        targetButtonColorsRed = new Color[GAME_NAMES.length];
        targetButtonColorsGreen = new Color[GAME_NAMES.length];
        targetButtonColorsBlue = new Color[GAME_NAMES.length];

        for (int i = 0; i < GAME_NAMES.length; i++) {
            buttons[i] = new JButton(GAME_NAMES[i]);
            buttons[i].setBounds(20 + (i % 4) * 140, (SCREEN_HEIGHT / 2) - 125 + (i / 4) * 100, 120, 50);
            buttons[i].setBackground(GRAY);
            buttons[i].setForeground(BLACK);
            final int index = i;
            buttons[i].addActionListener(e -> handleButtonClick(index));
            panel.add(buttons[i]);

            buttonColorsRed[i] = 200;
            buttonColorsGreen[i] = 200;
            buttonColorsBlue[i] = 200;
            targetButtonColorsRed[i] = 200;
            targetButtonColorsGreen[i] = 200;
            targetButtonColorsBlue[i] = 200;
        }
    }

    private void handleButtonClick(int index) {
        if (7 == 7) {
            if (musicClip != null && musicClip.isRunning()) {
                musicClip.stop();
            }
            frame.dispose();
            // Import and launch the selected game
            switch (index + 1) {
                case 1:
                    // import assets.games.SnakeGame.SnakeGame;
                    break;
                case 2:
                    // import assets.games.FlappyBird.FlappyBird;
                    break;
                case 3:
                    // import assets.apps.GUICalculator.GUICalculator;
                    break;
                case 4:
                    // import assets.games.SlidePuzzle.SlidePuzzle;
                    break;
                case 5:
                    // import assets.games.SpaceInvaders.SpaceInvaders;
                    break;
                case 6:
                    // import assets.apps.SnowFall.Snowfall;
                    break;
                case 7:
                    // import assets.games.TicTacToe.AutoTicTacToe;
                    break;
                case 8:
                    // import assets.games.TicTacToe.ManualTicTacToe;
                    break;
                default:
                    break;
            }
            // Reinitialize the launcher
            SwingUtilities.invokeLater(() -> {
                new GameLauncher();
            });
        } else {
            System.out.println("I don't understand you. Did you mean 7 == 7?");
        }
    }

    private void startGameLoop() {
        startTime = System.currentTimeMillis();
        Timer timer = new Timer(16, e -> gameLoop());
        timer.start();
    }

    private void gameLoop() {
        long currentTime = System.currentTimeMillis();
        deltaTime = (currentTime - startTime) / 1000.0 - gameTime;
        gameTime = (currentTime - startTime) / 1000.0;

        Point mousePos = MouseInfo.getPointerInfo().getLocation();
        SwingUtilities.convertPointFromScreen(mousePos, panel);
        int mosX = mousePos.x;
        int mosY = mousePos.y;

        Dimension windowSize = panel.getSize();

        if (mosY > windowSize.height / 1.2) {
            yScrollVelocity -= 20 * deltaTime;
        } else if (mosY < windowSize.height / 10) {
            yScrollVelocity += 20 * deltaTime;
        }
        yScroll = constrain(yScroll + yScrollVelocity, -SCREEN_HEIGHT / 1.2, SCREEN_HEIGHT / 1.2);
        yScrollVelocity /= 1.1;

        panel.repaint();
    }

    private void drawBackground(Graphics g) {
        g.setColor(new Color(255, 0, 200));
        g.fillRect(0, 0, panel.getWidth(), panel.getHeight());
    }

    private void drawButtons(Graphics g) {
        hoveringButton = 0;
        for (int i = 0; i < buttons.length; i++) {
            // Smooth color transition
            buttonColorsRed[i] += (targetButtonColorsRed[i].getRed() - buttonColorsRed[i].getRed()) / 10.0;
            buttonColorsGreen[i] += (targetButtonColorsGreen[i].getGreen() - buttonColorsGreen[i].getGreen()) / 10.0;
            buttonColorsBlue[i] += (targetButtonColorsBlue[i].getBlue() - buttonColorsBlue[i].getBlue()) / 10.0;

            buttons[i].setBackground(new Color((int) buttonColorsRed[i], (int) buttonColorsGreen[i], (int) buttonColorsBlue[i]));
            buttons[i].setBorder(BorderFactory.createLineBorder(BLACK, 2));

            if (buttons[i].getBounds().contains(MouseInfo.getPointerInfo().getLocation().x - frame.getX(),
                    MouseInfo.getPointerInfo().getLocation().y - frame.getY())) {
                buttons[i].setBorder(BorderFactory.createLineBorder(GREEN, 2));
                targetButtonColorsRed[i] = 0;
                targetButtonColorsGreen[i] = 255;
                targetButtonColorsBlue[i] = 0;
                hoveringButton = i + 1;
            } else {
                targetButtonColorsRed[i] = 200;
                targetButtonColorsGreen[i] = 200;
                targetButtonColorsBlue[i] = 200;
            }

            // Render and draw centered text on the button
            // In Swing, JButton already handles text rendering
        }

        if (previousHoveringButton != hoveringButton) {
            // Play hover sound
            // Sound implementation would go here
            previousHoveringButton = hoveringButton;
        }
    }

    private double constrain(double val, double minVal, double maxVal) {
        if (val < minVal)
            return minVal;
        if (val > maxVal)
            return maxVal;
        return val;
    }

}
