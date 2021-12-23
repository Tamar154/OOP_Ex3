import api.DirectedWeightedGraphAlgorithms;
import api.EdgeData;
import api.NodeData;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.Iterator;

public class MyPanel extends JPanel implements MouseListener {
    private DirectedWeightedGraphAlgorithms alg;
    private int width;
    private int height;
    private double x = 0;
    private double y = 0;
//    AffineTransform tx = new AffineTransform();
//    Line2D.Double line = new Line2D.Double(0,0,100,100);
//    Polygon arrowHead = new Polygon();


    public MyPanel(DirectedWeightedGraphAlgorithms alg, int width, int height) {
        this.width = width - 150;
        this.height = height - 150;
        this.alg = alg;
//        arrowHead.addPoint( 0,5);
//        arrowHead.addPoint( -5, -5);
//        arrowHead.addPoint( 5,-5);
    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponents(g);
        Graphics2D gr = (Graphics2D) g;
        gr.setColor(new Color(75, 0, 130));
        gr.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        Iterator<NodeData> iter = alg.getGraph().nodeIter();
        while (iter.hasNext()) {
            NodeData temp = iter.next();
            int xPixel = (int) scaleX(temp.getLocation().x());
            int yPixel = (int) scaleY(temp.getLocation().y());
            g.fillOval(xPixel, yPixel, 22, 22);
        }
        Iterator<EdgeData> iter2 = alg.getGraph().edgeIter();
        while (iter2.hasNext()) {
            gr.setColor(Color.black);
            EdgeData temp = iter2.next();
            NodeData currFrom = alg.getGraph().getNode(temp.getSrc());
            NodeData currTo = alg.getGraph().getNode(temp.getDest());
            double Xsrc = scaleX(currFrom.getLocation().x());
            double Ysrc = scaleY(currFrom.getLocation().y());
            double Xdst = scaleX(currTo.getLocation().x());
            double Ydst = scaleY(currTo.getLocation().y());
            g.drawLine(((int) Xsrc + 10), (int) Ysrc + 10, (int) Xdst + 10, (int) Ydst + 10);
//            tx.setToIdentity();
//            double angle = Math.atan2(((int) Ydst + 10) -( (int) Ysrc + 10), ((int) Xdst + 10) - ((int) Xsrc + 10));
//            tx.translate((int) Xdst + 10, (int) Ydst + 10);
//            tx.rotate((angle - Math.PI/ 2d));
//            Graphics2D g2d = (Graphics2D) g.create();
//            g2d.setTransform(tx);
//            g2d.fill(arrowHead);
        }

    }
//    private void drawArrowHead (Graphics2D g2d){
//        tx.setToIdentity();
//        double angle = Math.atan2(line.y2 - line.y1, line.x2 - line.x1);
//        tx.translate(line.x2, line.y2);
//        tx.rotate((angle - Math.PI / 2d));
//        Graphics2D g = (Graphics2D) g2d.create();
//        g.setTransform(tx);
//        g.fill(arrowHead);
//    }

    private double scaleX(double x) {
        return this.width * (x - MinX(alg.getGraph().nodeIter())) / (this.MaxX(alg.getGraph().nodeIter()) - MinX(alg.getGraph().nodeIter()));

    }

    private double scaleY(double y) {
        return this.height * (MaxY(alg.getGraph().nodeIter()) - y) / (this.MaxY(alg.getGraph().nodeIter()) - MinY(alg.getGraph().nodeIter()));
    }

    private double MaxX(Iterator<NodeData> iter) {
        double max = Double.MIN_VALUE;
        double tmp = 0;
        while (iter.hasNext()) {
            tmp = iter.next().getLocation().x();
            if (tmp > max) {
                max = tmp;
            }
        }
        return max;
    }

    private double MinX(Iterator<NodeData> iter) {
        double min = Double.MAX_VALUE;
        double tmp = 0;
        while (iter.hasNext()) {
            tmp = iter.next().getLocation().x();
            if (tmp < min) {
                min = tmp;
            }
        }
        return min;
    }

    private double MaxY(Iterator<NodeData> iter) {
        double max = 0;
        double tmp = 0;
        while (iter.hasNext()) {
            tmp = iter.next().getLocation().y();
            if (tmp > max) {
                max = tmp;
            }
        }
        return max;
    }

    private double MinY(Iterator<NodeData> iter) {
        double min = Double.MAX_VALUE;
        double tmp = 0;
        while (iter.hasNext()) {
            tmp = iter.next().getLocation().y();
            if (tmp < min) {
                min = tmp;
            }
        }
        return min;
    }


    @Override
    public void mouseClicked(MouseEvent e) {

    }

    @Override
    public void mousePressed(MouseEvent e) {

    }

    @Override
    public void mouseReleased(MouseEvent e) {

    }

    @Override
    public void mouseEntered(MouseEvent e) {

    }

    @Override
    public void mouseExited(MouseEvent e) {

    }
}
